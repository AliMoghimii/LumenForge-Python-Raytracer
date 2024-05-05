from Color import Color

import math

class MaterialMonochrome:

    def __init__(self, color = Color.HexToRgb("#FFFFFF"), ambient=0.05, diffuse=1.0, specular=1.0, reflection=0.5,):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection

    def colorBlendingProperties(self, position):
        return self.color
    
class MaterialCheckered:

    def __init__(self, color1 = Color.HexToRgb("#FFFFFF"), color2 = Color.HexToRgb("#000000"), ambient=0.05, diffuse=1.0, specular=1.0, reflection=0.5):
        self.color1 = color1
        self.color2 = color2
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.reflection = reflection

    def colorBlendingProperties(self, position):
        if math.floor((position.x + 5.0) * 3.0) % 2 == int(position.z * 3.0) % 2:
            return self.color1
        else:
            return self.color2