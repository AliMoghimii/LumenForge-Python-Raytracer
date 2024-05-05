from Vector3D import Vector3D
from Color import Color
from Image import Image
from Ray import Ray

class RenderEngine:

    SHADED = True;
    SHADOWS = True;
    MAXDEPTH = 5
    MINDISPLACEMENT = 0.0001

    def render(self, scene, SHADED, SHADOWS):
        self.SHADED = SHADED
        self.SHADOWS = SHADOWS;
        
        width = scene.width
        height = scene.height
        aspectRatio = float(width) / height

        x0 = -1.0
        x1 = +1.0
        xdelta = (x1 - x0) / (width - 1)

        y0 = -1.0 / aspectRatio
        y1 = +1.0 / aspectRatio
        ydelta = (y1 - y0) / (height - 1)

        camera = scene.camera
        pixels = Image(width, height)

        for j in range(height):
            y = y0 + j * ydelta
            for i in range(width):
                x = x0 + i * xdelta
                ray = Ray(camera, Vector3D(x,y) - camera)
                pixels.setPixel(i, j, self.raytrace(ray, scene))
            print("Rendering: In Progress (", "{:0.0f}%".format(float(j)/float(height) * 100), ")", end="\r")
        print("Rendering: Completed Successfully (100%)")    
        return pixels

#function in charge of calculating all the raytracing needs    
    def raytrace(self, ray, scene, depth = 0):
        color = Color(0,0,0)
        distanceHit, objectHit = self.rayCollision(ray, scene)
        if objectHit is None:
            return color
        hitPosition = ray.origin + ray.direction * distanceHit
        hitNormal = objectHit.norm(hitPosition)
        color += self.colorBlending(objectHit, hitPosition, hitNormal, scene)
        if depth < self.MAXDEPTH :
            newRayPosition = hitPosition + hitNormal * self.MINDISPLACEMENT
            newRayDirection = ray.direction - 2 * ray.direction.dot(hitNormal) * hitNormal
            newRay = Ray(newRayPosition, newRayDirection)

            #Attentuation process of the ray (reducing the intensity of hitRays when hitting a surface) using the relfection coeff
            color += self.raytrace(newRay, scene, depth+1) * objectHit.material.reflection

        return color

#find nearest hit position (object hit by ray)
    def rayCollision(self, ray, scene):
        distanceMin = None
        objectHit = None

        for object in scene.objects:
            distance = object.intersects(ray)
            if distance is not None and (objectHit is None or distance < distanceMin):
                distanceMin = distance
                objectHit = object
        return (distanceMin, objectHit)

#recursive color calculation in the simulation (when bouncing off)        
    def colorBlending (self, objectHit, hitPosition, hitNormal, scene):  
        if not self.SHADED :
            return objectHit.material.color

        objectHitMaterial = objectHit.material  
        objectHitColor = objectHitMaterial.colorBlendingProperties(hitPosition)
        rayToCamera =  Ray(hitPosition, scene.camera - hitPosition, False)
        newColor = objectHitMaterial.ambient * Color.HexToRgb("#000000")

        for light in scene.lights:
            
            rayToLight = Ray(hitPosition, light.position - hitPosition)

            if not self.SHADOWS :
                newColor += self.lambertianShading(objectHitMaterial, objectHitColor, hitNormal, rayToLight)
                newColor += self.blingPhongShading(light, objectHitMaterial, hitNormal, rayToLight, rayToCamera, 50)
            else :
                (dist, hit) = self.rayCollision(rayToLight, scene)                  
                if hit is None or (dist > (light.position - hitPosition).mag()): 
                    newColor += self.lambertianShading(objectHitMaterial, objectHitColor, hitNormal, rayToLight)
                    newColor += self.blingPhongShading(light, objectHitMaterial, hitNormal, rayToLight, rayToCamera, 50)
            
        return newColor

    def lambertianShading(self, objectHitMaterial, objectHitColor, hitNormal, rayToLight):
        return objectHitColor * objectHitMaterial.diffuse * max(hitNormal.dot(rayToLight.direction), 0)
    
    def blingPhongShading(self, light, objectHitMaterial, hitNormal, rayToLight, rayToCamera, specularExponent):
        halfVector = (rayToLight.direction + rayToCamera.direction).norm()
        return light.color * objectHitMaterial.specular * max(hitNormal.dot(halfVector), 0) ** specularExponent

