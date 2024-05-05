from Image import Image
from Color import Color

def main():

    WIDTH = 3
    HEIGHT = 3

    image = Image(WIDTH,HEIGHT)

    colorRed = Color(1,0,0)
    colorGreen = Color(0,1,0)
    colorBlue = Color(0,0,1)

    image.setPixel(0, 0, colorRed);
    image.setPixel(1, 0, colorGreen);
    image.setPixel(2, 0, colorBlue);

    image.setPixel(0, 1, colorRed + colorGreen);
    image.setPixel(1, 1, colorBlue + colorGreen);
    image.setPixel(2, 1, colorBlue + colorRed);

    image.setPixel(0, 2, colorRed + colorGreen + colorBlue);
    image.setPixel(1, 2, colorRed + Color(0, 0.5, 0));
    image.setPixel(2, 2, colorRed * 0.001);

    with open("00 - Export Test.ppm", "w") as imgFile:
        image.exportImage(imgFile)

if __name__ == "__main__":
    main()