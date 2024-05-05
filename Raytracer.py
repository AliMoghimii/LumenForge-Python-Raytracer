from Vector3D import Vector3D
from Color import Color
from Material import MaterialMonochrome, MaterialCheckered
from Light import PointLight
from Object3D import Object3DSphere
from Scene import Scene
from Engine import RenderEngine

def main():

    # Render Setting
    WIDTH = 1280
    HEIGHT = 720
    SHADOWS = True
    SHADED = True

    camera = Vector3D(0, -0.4, -1)

    objects = [
        Object3DSphere(Vector3D(0, 10000.5, 1), 10000.0, MaterialMonochrome(Color.HexToRgb("#111111"), ambient = 0.2, reflection = 0.2)),
        Object3DSphere(Vector3D(-0.25, 0, 0.6), 0.5, MaterialMonochrome(Color.HexToRgb("#FF0000"))),
        Object3DSphere(Vector3D(-0.15, -0.1, 0.15), 0.1, MaterialMonochrome(Color.HexToRgb("#FFFFFF"), reflection = 0.01)),
        Object3DSphere(Vector3D(-0.12, -0.12, 0.05), 0.05, MaterialMonochrome(Color.HexToRgb("#000000"), reflection = 0.01)),
        Object3DSphere(Vector3D(-0.4, -0.1, 0.15), 0.1, MaterialMonochrome(Color.HexToRgb("#FFFFFF"), reflection = 0.01)),
        Object3DSphere(Vector3D(-0.37, -0.12, 0.05), 0.05, MaterialMonochrome(Color.HexToRgb("#000000"), reflection = 0.01)),
        Object3DSphere(Vector3D(1.3, -0.15, 1), 0.75, MaterialMonochrome(Color.HexToRgb("#FFFF00"))),
        Object3DSphere(Vector3D(1, -1.85, 8), 0.75, MaterialMonochrome(Color.HexToRgb("#00FF00"))),
        Object3DSphere(Vector3D(-5, 3, 5), 5, MaterialCheckered(Color.HexToRgb("#0000FF"), Color.HexToRgb("#FFFFFF"))),
    ]

    lights = [
        PointLight(Vector3D(-1, -15, -1), Color.HexToRgb("#FFFFFF")),
        PointLight(Vector3D(2, -1, -10), Color.HexToRgb("#FFACF4"))
    ]
    
    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)

    engine = RenderEngine()
    image = engine.render(scene, SHADED, SHADOWS) 

    with open("# - Rendered Image.ppm", "w") as imgFile:
        image.exportImage(imgFile)

if __name__ == "__main__":
    main()
