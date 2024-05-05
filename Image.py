class Image:

    def __init__(self, width, height):
        self.width = width;
        self.height = height;
        self.pixels = [[None for _ in range(width)] for _ in range(height)]

    def setPixel(self, x, y, color): 
        self.pixels[y][x] = color

    def toByte(self, character):
        return round(max(min(character * 255, 255), 0))

    def exportImage(self, file):
        file.write("P3 {} {}\n255\n".format(self.width, self.height))
        for row in self.pixels:
            for color in row:
                file.write("{} {} {} ".format(self.toByte(color.r), self.toByte(color.g), self.toByte(color.b)))
            file.write("\n")
        

