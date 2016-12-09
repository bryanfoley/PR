import math
from shapeClass import Shape
from pointClass import Point

class Circle(Shape):

    def __init__(self,x,y,r=1):
        Shape._shapeCount +=1
        self._shapeNum = Shape._shapeCount
        self._shapeName = __class__.__name__
        self._r = math.fabs(r)
        self._point = Point(x,y)
        self._COM = self._point.getPoint()

    def __del__(self):
        class_name = self.__class__.__name__
        Shape._shapeCount-=1

    def setRadius(self,r):
        self._r = r
    
    def x(self):
        return self._point.x()

    def y(self):
        return self._point.y()

    def getRadius(self):
        return self._r

    def getWidth(self):
        return self._r*2.0

    def getHalfWidth(self):
        return self._r

    def getHeight(self):
        return self._r*2.0

    def getHalfHeight(self):
        return self._r

    def getCOM(self):
        return self._point.getPoint()

    def setCOM(self,x,y):
        return self._point.setPoint(x,y)

    def getShapeNum(self):
        return self._shapeNum

    def getName(self):
        return self._shapeName