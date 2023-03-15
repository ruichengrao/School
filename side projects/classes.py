import math

class Point:
    #class constructor
    def __init__(self,x = 0,y = 0) -> None:
        self.x = x
        self.y = y


        def distance(self, p2):
            dx = self.x - p2.x
            dy = self.x - p2.y
            sqdx = dx**2
            sqdy = dy**2
            addedDist = sqdx + sqdy
            Distance = math.sqrt(addedDist)
            return Distance

        def __str__(self):
            return "My x is " + str(self.x) + " and my y is " + str(self.y) + "."
        




    