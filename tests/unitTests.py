import unittest
import sys

sys.path.append('../')
import assignment
from shapeClass import Shape
from pointClass import Point
from circleClass import Circle
from quadrilateralClass import Quadrilateral
from squareClass import Square
from rectangleClass import Rectangle

class TestCircularCollisions(unittest.TestCase):

	def setUp(self):
		self.cars_x = [1.0,1.5]
		self.cars_y = self.cars_x
		self.cars_width = [1.0,1.0]
		self.cars_height = [1.0,1.0]
		self.cars_is_circular = True
		self.result = []

	def test_A001_overlap(self):
		self.result = assignment.get_intersections(self.cars_x, self.cars_y,self.cars_width,self.cars_height, self.cars_is_circular)
		self.assertEqual([(0,1)],self.result)
		
	def test_A002_no_overlap(self):
		self.cars_x = [1.0,2.0]
		self.cars_y = self.cars_x
		self.result = assignment.get_intersections(self.cars_x, self.cars_y,self.cars_width,self.cars_height, self.cars_is_circular)
		self.assertEqual([],self.result)

	def test_A003_maximum_overlap(self):
		self.cars_x = [1.0,1.0]
		self.cars_y = self.cars_x
		self.result = assignment.get_intersections(self.cars_x, self.cars_y,self.cars_width,self.cars_height, self.cars_is_circular)
		self.assertEqual([(0,1)],self.result)
		
	def test_A004_maximum_overlap(self):
		self.cars_x = [-1.0,-1.0]
		self.cars_y = self.cars_x
		self.result = assignment.get_intersections(self.cars_x, self.cars_y,self.cars_width,self.cars_height, self.cars_is_circular)
		self.assertEqual([(0,1)],self.result)
		
class TestRectangularCollisions(unittest.TestCase):

	def setUp(self):
		self.cars_x = [1.0,1.5]
		self.cars_y = self.cars_x
		self.cars_width = [1.0,1.0]
		self.cars_height = [1.0,1.0]
		self.cars_is_circular = False
		self.result = []

	def test_B001_overlap(self):
		self.result = assignment.get_intersections(self.cars_x, self.cars_y,self.cars_width,self.cars_height, self.cars_is_circular)
		self.assertEqual([(0,1)],self.result)
		
	def test_B002_no_overlap(self):
		self.cars_x = [1.0,2.0]
		self.cars_y = self.cars_x
		self.result = assignment.get_intersections(self.cars_x, self.cars_y,self.cars_width,self.cars_height, self.cars_is_circular)
		self.assertEqual([],self.result)
		
	def test_B003_maximum_overlap(self):
		self.cars_x = [1.0,1.0]
		self.cars_y = self.cars_x
		self.result = assignment.get_intersections(self.cars_x, self.cars_y,self.cars_width,self.cars_height, self.cars_is_circular)
		self.assertEqual([(0,1)],self.result)
		
class TestRectangularCircularCollisions(unittest.TestCase):

	def setUp(self):
		self.cars_x = [1.0,1.5]
		self.cars_y = self.cars_x
		self.cars_width = [1.0,1.0]
		self.cars_height = [1.0,1.0]
		self.cars_is_circular = [True,False]
		self.result = []

	def test_C001_overlap_circle_rectangle(self):
		self.result = assignment.get_intersections(self.cars_x, self.cars_y,self.cars_width,self.cars_height, self.cars_is_circular)
		self.assertEqual([(0,1)],self.result)
		
	def test_C002_no_overlap_circle_rectangle(self):
		self.cars_x = [1.0,2.0]
		self.cars_y = self.cars_x
		self.result = assignment.get_intersections(self.cars_x, self.cars_y,self.cars_width,self.cars_height, self.cars_is_circular)
		self.assertEqual([],self.result)
		
	def test_C003_overlap_rectangle_circle(self):
		self.cars_is_circular = [False,True]
		self.result = assignment.get_intersections(self.cars_x, self.cars_y,self.cars_width,self.cars_height, self.cars_is_circular)
		self.assertEqual([(0,1)],self.result)
		
	def test_C004_no_overlap_rectangle_circle(self):
		self.cars_is_circular = [False,True]
		self.cars_x = [1.0,2.0]
		self.cars_y = self.cars_x
		self.result = assignment.get_intersections(self.cars_x, self.cars_y,self.cars_width,self.cars_height, self.cars_is_circular)
		self.assertEqual([],self.result)
		
	def test_C005_maximum_overlap_rectangle_circle(self):
		self.cars_is_circular = [False,True]
		self.cars_x = [1.0,1.0]
		self.cars_y = self.cars_x
		self.result = assignment.get_intersections(self.cars_x, self.cars_y,self.cars_width,self.cars_height, self.cars_is_circular)
		self.assertEqual([(0,1)],self.result)

class TestShapeClass(unittest.TestCase):
	def setUp(self):
		self.s1 = Shape()

	def tearDown(self):
		del self.s1

	def test_D001_test_shape_creation(self):
		result = self.s1.getShapeCount()
		self.assertEqual(result,0)

	def test_D002_test_shape_get_COM(self):
		result = self.s1.getCOM()
		self.assertEqual(result,"Shape object is returning COM")

class TestPointClass(unittest.TestCase):
	def setUp(self):
		self.p1 = Point()
		self.p2 = Point(1.0,1.0)

	def tearDown(self):
		del self.p1
		del self.p2

	def test_E001_test_point_creation(self):
		result1 = self.p1.getShapeCount()
		self.assertEqual(result1,0)
		result2 = self.p1.x()
		self.assertEqual(result2,0.0)
		result3 = self.p1.y()
		self.assertEqual(result3,0.0)
		result4 = self.p1.getPoint()
		self.assertEqual(result4,(0.0,0.0))
		self.p1.setPoint(2.0,2.0)
		result5 = self.p1.getPoint()
		self.assertEqual(result5,(2.0,2.0))
		result6 = self.p2.getPoint()
		self.assertEqual(result6,(1.0,1.0))

	def test_E002_test_point_get_COM(self):
		result = self.p1.getCOM()
		self.assertEqual(result,"Point object is returning COM")
		result = self.p2.getCOM()
		self.assertEqual(result,"Point object is returning COM")

class TestCircleClass(unittest.TestCase):
	def setUp(self):
		self.c1 = Circle(1.0,0.0,0.0)
		self.c2 = Circle(1.0,1.0,1.0)

	def tearDown(self):
		del self.c1
		del self.c2

	def test_F001_test_circle_creation(self):
		result1 = self.c1.getShapeCount()
		self.assertEqual(result1,2)
		result2 = self.c1.getRadius()
		self.assertEqual(result2,1.0)
		result3 = self.c1.getWidth()
		self.assertEqual(result3,2.0)
		result4 = self.c1.getHeight()
		self.assertEqual(result4,2.0)
		result5 = self.c1.getHalfWidth()
		self.assertEqual(result5,1.0)
		result6 = self.c1.getHalfHeight()
		self.assertEqual(result6,1.0)
		self.c2.setRadius(3.0)
		result7 = self.c2.getRadius()
		self.assertEqual(result7,3.0)

	def test_F002_test_point_get_COM(self):
		result1 = self.c1.getCOM()
		self.assertEqual(result1,(0.0,0.0))
		self.c2.setCOM(2.0,2.0)
		result2 = self.c2.getCOM()
		self.assertEqual(result2,(2.0,2.0))

class TestQuadrilateralClass(unittest.TestCase):
	def setUp(self):
		self.q1 = Quadrilateral()
		self.q2 = Quadrilateral((-4,2),(4,2),(4,-2),(-4,-2),1.5708,1.5709,1.5710,1.5711)

	def tearDown(self):
		del self.q1
		del self.q2

	def test_G001_test_quadrilateral_implicit_creation(self):
		result1 = self.q1.getShapeCount()
		self.assertEqual(result1,0)
		result2 = self.q1.getTopLeft()
		self.assertEqual(result2,(-2,1))
		result3 = self.q1.getTopRight()
		self.assertEqual(result3,(2,1))
		result4 = self.q1.getBottomRight()
		self.assertEqual(result4,(2,-1))
		result5 = self.q1.getBottomLeft()
		self.assertEqual(result5,(-2,-1))
		result6 = self.q1.getAngleA()
		self.assertEqual(result6,1.5708)
		result7 = self.q1.getAngleB()
		self.assertEqual(result7,1.5708)
		result8 = self.q1.getAngleC()
		self.assertEqual(result8,1.5708)
		result9 = self.q1.getAngleD()
		self.assertEqual(result9,1.5708)
		result10 = self.q1.getCOM()
		self.assertEqual(result10,"Quadrilateral object is returning COM")

	def test_G002_test_quadriilateral_explicit_creation(self):
		result1 = self.q2.getShapeCount()
		self.assertEqual(result1,0)
		result2 = self.q2.getTopLeft()
		self.assertEqual(result2,(-4,2))
		result3 = self.q2.getTopRight()
		self.assertEqual(result3,(4,2))
		result4 = self.q2.getBottomRight()
		self.assertEqual(result4,(4,-2))
		result5 = self.q2.getBottomLeft()
		self.assertEqual(result5,(-4,-2))
		result6 = self.q2.getAngleA()
		self.assertEqual(result6,1.5708)
		result7 = self.q2.getAngleB()
		self.assertEqual(result7,1.5709)
		result8 = self.q2.getAngleC()
		self.assertEqual(result8,1.5710)
		result9 = self.q2.getAngleD()
		self.assertEqual(result9,1.5711)
		result10 = self.q2.getCOM()
		self.assertEqual(result10,"Quadrilateral object is returning COM")

	def test_G003_test_quadriilateral_set(self):
		self.q2.setQuadrilateral((-8,2),(8,2),(8,-2),(-8,-2),1.5708,1.5709,1.5710,1.5711)
		result1 = self.q2.getShapeCount()
		self.assertEqual(result1,0)
		result2 = self.q2.getQuadrilateral()
		self.assertEqual(result2, [(-8,2),(8,2),(8,-2),(-8,-2),1.5708,1.5709,1.5710,1.5711])

class TestSquareClass(unittest.TestCase):
	def setUp(self):
		self.sq1 = Square(2.0,2.0,2.0)
		self.sq2 = Square(1.0,1.0,1.0)

	def tearDown(self):
		del self.sq1
		del self.sq2

	def test_H001_test_square_creation(self):
		result1 = self.sq1.getShapeCount()
		self.assertEqual(result1,2)
		result2 = self.sq1.x()
		self.assertEqual(result2,2.0)
		result3 = self.sq1.y()
		self.assertEqual(result3,2.0)
		result4 = self.sq1.getWidth()
		self.assertEqual(result4,2.0)
		result5 = self.sq1.getHalfWidth()
		self.assertEqual(result5,1.0)
		result6 = self.sq1.getHeight()
		self.assertEqual(result6,2.0)
		result7 = self.sq1.getHalfHeight()
		self.assertEqual(result7,1.0)
		result8 = self.sq1.getCOM()
		self.assertEqual(result8,(2.0,2.0))
		result9 = self.sq1.getShapeNum()
		self.assertEqual(result9,1)

	def test_H002_test_square_get_set_COM(self):
		result1 = self.sq2.getCOM()
		self.assertEqual(result1,(1.0,1.0))
		self.sq2.setCOM(4.0,4.0)
		result2 = self.sq2.getCOM()
		self.assertEqual(result2,(4.0,4.0))

class TestRectangleClass(unittest.TestCase):
	def setUp(self):
		self.rec1 = Rectangle(2.0,2.0,2.0,3.0)
		self.rec2 = Rectangle(1.0,1.0,1.0,4.0)

	def tearDown(self):
		del self.rec1
		del self.rec2

	def test_I001_test_rectangle_creation(self):
		result1 = self.rec1.getShapeCount()
		self.assertEqual(result1,2)
		result2 = self.rec1.x()
		self.assertEqual(result2,2.0)
		result3 = self.rec1.y()
		self.assertEqual(result3,2.0)
		result4 = self.rec1.getWidth()
		self.assertEqual(result4,2.0)
		result5 = self.rec1.getHalfWidth()
		self.assertEqual(result5,1.0)
		result6 = self.rec1.getHeight()
		self.assertEqual(result6,3.0)
		result7 = self.rec1.getHalfHeight()
		self.assertEqual(result7,1.5)
		result8 = self.rec1.getCOM()
		self.assertEqual(result8,(2.0,2.0))
		result9 = self.rec1.getShapeNum()
		self.assertEqual(result9,1)

	def test_I002_test_rectangle_get_set_COM(self):
		result1 = self.rec2.getCOM()
		self.assertEqual(result1,(1.0,1.0))
		self.rec2.setCOM(4.0,4.0)
		result2 = self.rec2.getCOM()
		self.assertEqual(result2,(4.0,4.0))

if __name__ == '__main__':
    unittest.main()