class Square (Shape) :
	def __init__(self) :
		self._shapeNum = None # int
		self._quad = None # Quadrilateral
		self._side = None # double
		self._COM = None # tuple
		self._shapeName = Square # string
		pass
	def Square (self, x, y, side) :
		# returns 
		pass
	def setSquare (self, x, y, side) :
		# returns 
		pass
	def getSquare (self, ) :
		# returns 
		pass
	def getHeight (self, _side) :
		# returns 
		pass
	def getWidth (self, _side) :
		# returns 
		pass
	def getHalfHeight (self, _side/2.0) :
		# returns 
		pass
	def getHalfWidth (self, _side/2.0) :
		# returns 
		pass
	def x (self, _x) :
		# returns 
		pass
	def y (self, _y) :
		# returns double
		pass
	def getCOM (self, ) :
		# returns 
		pass
	def getShapeNum (self, _shapeNum) :
		# returns 
		pass
	def getName (self, _shapeName) :
		# returns 
		pass
	def left (self, _quad._left) :
		# returns 
		pass
	def right (self, _quad._right) :
		# returns 
		pass
	def top (self, _quad._top) :
		# returns 
		pass
	def bottom (self, _quad._bottom) :
		# returns 
		pass
class Point (Shape) :
	def __init__(self) :
		self._x = 0.0 # double
		self._y = 0.0 # double
		pass
	def Point (self, x, y) :
		# returns 
		pass
	def setPoint (self, x, y) :
		# returns 
		pass
	def x (self, _x) :
		# returns double
		pass
	def y (self, _y) :
		# returns double
		pass
	def getPoint (self, _x,_y) :
		# returns tuple
		pass
	def getCOM (self) :
		# returns 
		pass
class Automobile :
	def __init__(self) :
		self.automobileCount = None # int
		pass
	def getAutomobileCount (self) :
		# returns int
		pass
	def getCOM (self) :
		# returns 
		pass
class Quadrilateral (Shape) :
	def __init__(self) :
		self._topLeft = None # Point
		self._topRight = None # Point
		self._bottomRight = None # Point
		self._bottomLeft = None # Point
		self._angleA = 1.5708 # double
		self._angleB = 1.5708 # double
		self._angleC = 1.5708 # double
		self._angleD = 1.5708 # double
		self._top = None # double
		self._bottom = None # double
		self._left = None # double
		self._right = None # double
		pass
	def Quadrilateral (self, A, B, C, D, thetaA, thetaB, thetaC, thetaD) :
		# returns 
		pass
	def getQuadrilateral (self) :
		# returns list
		pass
	def getTopLeft (self) :
		# returns Point
		pass
	def getTopRight (self) :
		# returns Point
		pass
	def getBottomRight (self) :
		# returns Point
		pass
	def getBottomLeft (self) :
		# returns Point
		pass
	def getAngleA (self) :
		# returns double
		pass
	def getAngleB (self) :
		# returns double
		pass
	def getAngleC (self) :
		# returns double
		pass
	def getAngleD (self) :
		# returns double
		pass
	def getCOM (self) :
		# returns 
		pass
	def getTop (self, _top) :
		# returns 
		pass
	def getBottom (self, _bottom) :
		# returns 
		pass
	def getLeft (self, _left) :
		# returns 
		pass
	def getRight (self, _right) :
		# returns 
		pass
class Shape :
	def __init__(self) :
		self.shapeCount = None # int
		pass
	def getShapeCount (self) :
		# returns int
		pass
	def getCOM (self) :
		# returns 
		pass
class Truck :
	def __init__(self) :
		self._autoNum = None # int
		self._autoName = None # string
		self._top = None # double
		self._bottom = None # double
		self._left = None # double
		self._right = None # double
		self._COM = None # tuple
		self._components = None # dict
		pass
	def Truck (self, x, y) :
		# returns 
		pass
	def getCOM (self, ) :
		# returns 
		pass
	def left (self, _left) :
		# returns 
		pass
	def right (self, _right) :
		# returns 
		pass
	def top (self, _top) :
		# returns 
		pass
	def bottom (self, _bottom) :
		# returns 
		pass
	def getName (self, _autoName) :
		# returns 
		pass
	def getNum (self, _autoNum) :
		# returns 
		pass
class Car (Automobile) :
	def __init__(self) :
		self._autoNum = None # int
		self._autoName = None # string
		self._top = None # double
		self._bottom = None # double
		self._left = None # double
		self._right = None # double
		self._COM = None # tuple
		self._components = None # dict
		pass
	def Car (self, x, y) :
		# returns 
		pass
	def getCOM (self, ) :
		# returns 
		pass
	def left (self, _left) :
		# returns 
		pass
	def right (self, _right) :
		# returns 
		pass
	def top (self, _top) :
		# returns 
		pass
	def bottom (self, _bottom) :
		# returns 
		pass
	def getName (self, _autoName) :
		# returns 
		pass
	def getNum (self, _autoNum) :
		# returns 
		pass
class Circle (Shape) :
	def __init__(self) :
		self._shapeNum = None # int
		self._r = None # double
		self._point = None # Point
		self._COM = None # tuple
		self._shapeName = Circle # string
		self._top = None # double
		self._bottom = None # double
		self._left = None # double
		self._right = None # double
		pass
	def Circle (self, x, y, r) :
		# returns 
		pass
	def setRadius (self, r) :
		# returns 
		pass
	def getRadius (self, _r) :
		# returns 
		pass
	def x (self, _x) :
		# returns 
		pass
	def y (self, _y) :
		# returns 
		pass
	def getWidth (self, _width) :
		# returns 
		pass
	def getName() (self, _shapeName) :
		# returns 
		pass
	def getHalfWidth (self, _width/2.0) :
		# returns 
		pass
	def getHeight (self, _height) :
		# returns 
		pass
	def getHalfHeight (self, _height/2.0) :
		# returns 
		pass
	def getCOM (self, ) :
		# returns 
		pass
	def setCOM (self, x, y) :
		# returns 
		pass
	def getShapeNum (self, _shapeNum) :
		# returns 
		pass
	def left (self, _left) :
		# returns double
		pass
	def right (self, _right) :
		# returns 
		pass
	def top (self, _top) :
		# returns 
		pass
	def bottom (self, _bottom) :
		# returns 
		pass
class Bus (Automobile) :
	def __init__(self) :
		self._autoNum = None # int
		self._autoName = None # string
		self._top = None # double
		self._bottom = None # double
		self._left = None # double
		self._right = None # double
		self._COM = None # tuple
		self._components = None # dict
		pass
	def Bus (self, x, y) :
		# returns 
		pass
	def getCOM (self, ) :
		# returns 
		pass
	def left (self, _left) :
		# returns 
		pass
	def right (self, _right) :
		# returns 
		pass
	def top (self, _top) :
		# returns 
		pass
	def bottom (self, _bottom) :
		# returns 
		pass
	def getName (self, _autoName) :
		# returns 
		pass
	def getNum (self, _autoNum) :
		# returns 
		pass
class Rectangle (Shape) :
	def __init__(self) :
		self._shapeNum = None # int
		self._quad = None # Quadrilateral
		self._width = None # double
		self._height = None # double
		self._COM = None # tuple
		self._shapeName = Rectangle # string
		pass
	def Rectangle (self, x, y, w, h) :
		# returns 
		pass
	def setRectangle (self, x, y, w, h) :
		# returns 
		pass
	def getRectangle (self, ) :
		# returns 
		pass
	def getHeight (self) :
		# returns double
		pass
	def getWidth (self) :
		# returns double
		pass
	def getHalfHeight (self) :
		# returns double
		pass
	def getHalfWidth (self) :
		# returns double
		pass
	def x (self) :
		# returns double
		pass
	def y (self) :
		# returns double
		pass
	def getCOM (self, ) :
		# returns 
		pass
	def getShapeNum (self, _shapeNum) :
		# returns 
		pass
	def getName() (self, _shapeName) :
		# returns 
		pass
	def left (self, _quad._left) :
		# returns 
		pass
	def right (self, _quad._right) :
		# returns 
		pass
	def top (self, _quad._top) :
		# returns 
		pass
	def bottom (self, _quad._bottom) :
		# returns 
		pass
