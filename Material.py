from Color import Color

class MaterialMonochrome:

    def __init__(self, color = Color.HexToRgb("#FFFFFF"), ambient=0.05, diffuse=1.0, specular=1.0):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular

    def colorBlendingProperties(self, position):
        return self.color