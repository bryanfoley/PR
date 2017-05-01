from shapeClass import Shape
from pointClass import Point

class Quadrilateral(Shape):
    def __init__(self,A=(-2.0,1.0),B=(2.0,1.0),C=(2.0,-1.0),D=(-2.0,-1.0),
                thetaA=1.5708,thetaB=1.5708,thetaC=1.5708,thetaD=1.5708):
        self._topLeft = Point()
        self._topRight = Point()
        self._bottomRight = Point()
        self._bottomLeft = Point()
        self._angleA = 0.0
        self._angleB = 0.0
        self._angleC = 0.0
        self._angleD = 0.0
        self.setQuadrilateral(A,B,C,D,thetaA,thetaB,thetaC,thetaD)

    def setQuadrilateral(self,A,B,C,D,thetaA,thetaB,thetaC,thetaD):
        self._topLeft.setPoint(A[0],A[1])
        self._topRight.setPoint(B[0],B[1])
        self._bottomRight.setPoint(C[0],C[1])
        self._bottomLeft.setPoint(D[0],D[1])
        self._angleA = thetaA
        self._angleB = thetaB
        self._angleC = thetaC
        self._angleD = thetaD
        self._top = max(A[1],B[1])
        self._bottom = min(C[1],D[1])
        self._left = min(A[0],D[0])
        self._right = max(B[0],C[0]) 

    def getQuadrilateral(self):
        return [self.getTopLeft(),self.getTopRight(),
               self.getBottomRight(), self.getBottomLeft(),
               self.getAngleA(),self.getAngleB(),
               self.getAngleC(), self.getAngleD()]

    def getTopLeft(self):
        return self._topLeft.getPoint()

    def getTopRight(self):
        return self._topRight.getPoint()

    def getBottomRight(self):
        return self._bottomRight.getPoint()

    def getBottomLeft(self):
        return self._bottomLeft.getPoint()

    def getAngleA(self):
        return self._angleA

    def getAngleB(self):
        return self._angleB

    def getAngleC(self):
        return self._angleC

    def getAngleD(self):
        return self._angleD

    def getCOM(self):
        pass

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def getTop(self):
        return self._top

    def getBottom(self):
        return self._bottom
