import math
from automobileClass import Automobile
from circleClass import Circle
from squareClass import Square
from rectangleClass import Rectangle

class Truck(Automobile):

    def __init__(self,x,y):
        Automobile._automobileCount += 1
        self._autoName = __class__.__name__
        self._autoNum = Automobile._automobileCount
        self._components = dict(body=Rectangle(x,y,20,10),
                                roof=Circle(x+10,y,5),
                                hood=Square(x+12.5,y-2.5,5),
                                wheel1=Circle(x-7,y-5,1),
                                wheel2=Circle(x+1.25,y-5,1))
        self._top = self._components[max(self._components,key = lambda i: self._components[i].top())].top()
        self._bottom = self._components[min(self._components,key = lambda i: self._components[i].bottom())].bottom()
        self._left = self._components[min(self._components,key = lambda i: self._components[i].left())].left()
        self._right = self._components[max(self._components,key = lambda i: self._components[i].right())].right()
        self._COM = (x,y)

    def __del__(self):
        class_name = self.__class__.__name__
        Automobile._automobileCount-=1
    def getCOM (self):
        return (self._COM[0], self._COM[1])

    def left (self):
        return self._left

    def right (self):
        return self._right

    def top (self):
        return self._top 

    def bottom (self):
        return self._bottom 

    def getAutoName (self):
        return self._autoName 

    def getAutoNum (self):
        return self._autoNum 

