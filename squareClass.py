from shapeClass import Shape
from quadrilateralClass import Quadrilateral

class Square(Shape):
    def __init__(self,x,y,side):
        Shape._shapeCount +=1
        self._shapeNum = Shape._shapeCount
        self._shapeName = __class__.__name__
        self._side = side
        self.createVertices(x,y)

    def __del__(self):
        class_name = self.__class__.__name__
        Shape._shapeCount-=1

    def createVertices(self,x,y):
        A = (x-self._side/2.0,y+self._side/2.0)
        B = (x+self._side/2.0,y+self._side/2.0)
        C = (x+self._side/2.0,y-self._side/2.0)
        D = (x-self._side/2.0,y-self._side/2.0)
        self._quad = Quadrilateral(A,B,C,D)
        self._COM = (x,y)

    def x(self):
        return self._COM[0]

    def y(self):
        return self._COM[1]

    def setCOM(self,x,y):
        self.createVertices(x,y)

    def getWidth(self):
        return self._side

    def getHalfWidth(self):
        return self._side/2.0

    def getHeight(self):
        return self._side

    def getHalfHeight(self):
        return self._side/2.0

    def getCOM(self):
        return self._COM

    def getShapeNum(self):
        return self._shapeNum

    def getName(self):
        return self._shapeName

    def left(self):
        return self._quad.getLeft()

    def right(self):
        return self._quad.getRight()

    def top(self):
        return self._quad.getTop()

    def bottom(self):
        return self._quad.getBottom()