import math

class Vector:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x;
        self.y = y;
        self.z = z;

    def __str__(self):
        return "({},{},{})".format(self.x, self.y, self.z)
    
    def dot(self, target):
        return self.x * target.x + self.y * target.y + self.z * target.z
    
    def mag(self):
        return math.sqrt(self.dot(self))
    
    def norm(self):
        return self/self.mag()
    
    def __add__(self, target):
        return Vector(self.x + target.x, self.y + target.y, self.z + target.z)
    
    def __sub__(self, target):
        return Vector(self.x - target.x, self.y - target.y, self.z - target.z)
    
    def __mul__(self, num):
        assert not isinstance(num, Vector)
        return Vector(self.x * num, self.y * num, self.z * num)
    
    def __rmul__(self, num):
        return self.__mul__(num)
    
    def __truediv__(self, num):
        assert not isinstance(num, Vector)
        return Vector(self.x / num, self.y / num, self.z / num)
