from Ray import Ray

from math import sqrt

class Object3DSphere:

    def __init__(self, center, radius, material):
        self.center = center;
        self.radius = radius; 
        self.material = material;

    def intersects(self, ray):
        rayDirection = Ray(self.center, ray.origin - self.center, False)

        #Quadratic Equation
        a = 1
        b = 2 * ray.direction.dot(rayDirection.direction)
        c = rayDirection.direction.dot(rayDirection.direction) - self.radius * self.radius

        discriminant = b * b - 4 * c

        if discriminant >= 0:
            dist = (-b - sqrt(discriminant)) / 2
            if dist > 0:
                return dist
        return None
    
    def norm(self, surfacePoint):
        return(surfacePoint - self.center).norm()