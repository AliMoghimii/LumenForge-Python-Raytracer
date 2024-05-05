from Color import Color

class PointLight:
    def __init__(self, position, color=Color.HexToRgb("#FFFFFF")):
        self.position = position
        self.color = color