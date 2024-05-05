class Ray:
    
    def __init__(self, origin, direction, normalize = True):
        self.origin = origin;
        if normalize :
            self.direction = direction.norm();
        else : 
            self.direction = direction;