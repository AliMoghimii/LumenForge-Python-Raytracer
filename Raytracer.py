from Vector3D import Vector3D
from Color import Color
from Material import MaterialMonochrome
from Light import PointLight
from Object3D import Object3DSphere
from Scene import Scene
from Engine import RenderEngine

def main():

    WIDTH = 640
    HEIGHT = 640

    camera = Vector3D(0,0,-1)

    sphereRadius = 0.2
    objects = [
        Object3DSphere(Vector3D(-0.5, -0.5, 0), sphereRadius, MaterialMonochrome(Color.HexToRgb("#FF0000"))),
        Object3DSphere(Vector3D(0, -0.5, 0), sphereRadius, MaterialMonochrome(Color.HexToRgb("#00FF00"))),
        Object3DSphere(Vector3D(0.5, -0.5, 0), sphereRadius, MaterialMonochrome(Color.HexToRgb("#0000FF"))),
        Object3DSphere(Vector3D(-0.5, 0, 0), sphereRadius, MaterialMonochrome(Color.HexToRgb("#FFFF00"))),
        Object3DSphere(Vector3D(0, 0, 0), sphereRadius, MaterialMonochrome(Color.HexToRgb("#00FFFF"))),
        Object3DSphere(Vector3D(0.5, 0, 0), sphereRadius, MaterialMonochrome(Color.HexToRgb("#FF00FF"))),
        Object3DSphere(Vector3D(-0.5, 0.5, 0), sphereRadius, MaterialMonochrome(Color.HexToRgb("#FFFFFF"))),
        Object3DSphere(Vector3D(0, 0.5, 0), sphereRadius, MaterialMonochrome(Color.HexToRgb("#FF8000"))),
        Object3DSphere(Vector3D(0.5, 0.5, 0), sphereRadius, MaterialMonochrome(Color.HexToRgb("#404040")))
        ]
    
    lights = [
        PointLight(Vector3D(0.3, -0.15, -0.25), Color.HexToRgb("#FFFFFF"))
        ]
    
    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)

    engine = RenderEngine()
    image = engine.render(scene, True) 

    with open("02 - Shading Test.ppm", "w") as imgFile:
        image.exportImage(imgFile)

if __name__ == "__main__":
    main()
