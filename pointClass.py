from shapeClass import Shape

class Point(Shape):
    def __init__(self,x=0.0,y=0.0):
        self._x = x
        self._y = y

    def __del__(self):
        class_name = self.__class__.__name__

    def setPoint(self,x,y):
        self._x = x
        self._y = y

    def x(self):
        return self._x

    def y(self):
        return self._y

    def getPoint(self):
        return (self._x,self._y)

    def getCOM(self):
        return "Point object is returning COM"