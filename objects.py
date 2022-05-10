class Point:
    '''
    A class to represent two-dimensional
    points.
    Attributes:
        x - a float
        y - a float
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class Circle:
    '''
    A class to represent a circle in the plane.
    Attributes:
        center - a point
        radius - a float
    '''
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

       

