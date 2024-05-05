class Color:

    def __init__(self, r=0.0, g=0.0, b=0.0):
        self.r = r;
        self.g = g;
        self.b = b;
    
    def HexToRgb(hexValue = "#000000"):
        r = int(hexValue[1:3], 16) / 255.0
        g = int(hexValue[3:5], 16) / 255.0
        b = int(hexValue[5:7], 16) / 255.0
        return Color(r, g, b)

    def __str__(self):
        return "({},{},{})".format(self.r, self.g, self.b)
    

    def __add__(self, target):
        return Color(self.r + target.r, self.g + target.g, self.b + target.b)
    
    def __sub__(self, target):
        return Color(self.r - target.r, self.g - target.g, self.b - target.b)
    
    def __mul__(self, num):
        assert not isinstance(num, Color)
        return Color(self.r * num, self.g * num, self.b * num)
    
    def __rmul__(self, num):
        return self.__mul__(num)
    
    def __truediv__(self, num):
        assert not isinstance(num, Color)
        return Color(self.r / num, self.g / num, self.b / num)
