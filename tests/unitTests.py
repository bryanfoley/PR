import unittest
import sys

sys.path.append('../')
sys.path.append('../src/shapes')
sys.path.append('../src/automobiles')
import assignment
from shapeClass import Shape
from pointClass import Point
from circleClass import Circle
from quadrilateralClass import Quadrilateral
from squareClass import Square
from rectangleClass import Rectangle
from automobileClass import Automobile
from carClass import Car
from truckClass import Truck
from busClass import Bus

class TestCircularCollisions(unittest.TestCase):
	#Test the function circleXcircle(ShapeA, ShapeB)

	def setUp(self):
		#Both circles initially have the same Centre of Mass and overlap perfectly
		self.c1 = Circle(1.0,1.0,1.0)
		self.c2 = Circle(1.0,1.0,1.0)

	def tearDown(self):
		del self.c1
		del self.c2

	def test_A001_maximum_overlap(self):
		'Perfect overlap'
		self.result = assignment.circleXcircle(self.c1,self.c2)
		self.assertEqual(True,self.result)
		
	def test_A002_no_overlap(self):
		'No overlap'
		self.c1.setCOM(9.0,9.0)
		self.result = assignment.circleXcircle(self.c1,self.c2)
		self.assertEqual(False,self.result)

	def test_A003_slight_overlap(self):
		'The circles overlap by an appreciable amount'
		self.c1.setCOM(1.5,1.5)
		self.result = assignment.circleXcircle(self.c1,self.c2)
		self.assertEqual(True,self.result)
		
	def test_A004_touching(self):
		'The circles are seperated by a distance equal to the sum of their radii'
		self.c1.setCOM(3.0,1.0)
		self.result = assignment.circleXcircle(self.c1,self.c2)
		self.assertEqual(True,self.result)

class TestQuadrilateralCollisions(unittest.TestCase):
	#Testing the function quadXquad(Shape A, Shape B)

	def setUp(self):
		#Both shapes initially have the same Centre of Mass
		self.sq1 = Square(0.0,0.0,1.0)
		self.rec1 = Rectangle(0,0,4,1.5)

	def tearDown(self):
		del self.sq1
		del self.rec1

	def test_B001_maximum_overlap(self):
		'Perfect overlap'
		self.result = assignment.quadXquad(self.sq1,self.rec1)
		self.assertEqual(True,self.result)
		
	def test_B002_no_overlap(self):
		'No overlap'
		self.rec1.setCOM(5.5,5.5)
		self.result = assignment.quadXquad(self.sq1,self.rec1)
		self.assertEqual(False,self.result)
		
	def test_B003_slight_overlap(self):
		'The Square and Rectangle overlap by an appreciable amount'
		self.rec1.setCOM(0.25,0.25)
		self.result = assignment.quadXquad(self.sq1,self.rec1)
		self.assertEqual(True,self.result)

	def test_B004_touching(self):
		'The bottom left corner of the Rectangle is touching the top right corner of the Square'
		self.rec1.setCOM(2.5,1.25)
		self.result = assignment.quadXquad(self.sq1,self.rec1)
		self.assertEqual(True,self.result)
		
class TestCircularQuadrilateralCollisions(unittest.TestCase):
	#Test the function quadXcircle(Shape A, Shape B)

	def setUp(self):
		#Both shapes initially have the same Centre of Mass
		self.c1 = Circle(0.0,0.0,1.0)
		self.sq1 = Square(0.0,0.0,1.0)

	def tearDown(self):
		del self.c1
		del self.sq1

	def test_C001_maximum_overlap(self):
		'Perfect overlap'
		self.result = assignment.quadXcircle(self.c1,self.sq1)
		self.assertEqual(True,self.result)
		
	def test_C002_no_overlap(self):
		'No overlap'
		self.c1.setCOM(5.5,5.5)
		self.result = assignment.quadXcircle(self.c1,self.sq1)
		self.assertEqual(False,self.result)
		
	def test_C003_slight_overlap(self):
		'The Circle and Square overlap by an appreciable amount'
		self.c1.setCOM(1.0,1.0)
		self.result = assignment.quadXcircle(self.c1,self.sq1)
		self.assertEqual(True,self.result)

	def test_C004_touching(self):
		'The Circle is just touching the top right corner of teh Square'
		self.c1.setCOM(1.5,1.5)
		self.result = assignment.quadXcircle(self.c1,self.sq1)
		self.assertEqual(True,self.result)

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
		self.assertEqual(type(self.s1),Shape)

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
		self.assertEqual(type(self.p1),Point)
		result = self.p2.getCOM()
		self.assertEqual(type(self.p2),Point)

class TestCircleClass(unittest.TestCase):
	def setUp(self):
		self.c1 = Circle(0.0,0.0,1.0)
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
		result8 = self.c1.getName()
		self.assertEqual(result8,'Circle')
		result9 = self.c1.top()
		self.assertEqual(result9,1.0)
		result10 = self.c1.bottom()
		self.assertEqual(result10,-1.0)
		result11 = self.c1.left()
		self.assertEqual(result11,-1.0)
		result12 = self.c1.right()
		self.assertEqual(result12,1.0)		

	def test_F002_test_circle_get_COM(self):
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
		self.assertEqual(type(self.q1),Quadrilateral)
		result11 = self.q1.getBottom()
		self.assertEqual(result11,-1.0)
		result12 = self.q1.getTop()
		self.assertEqual(result12,1.0)
		result13 = self.q1.getLeft()
		self.assertEqual(result13,-2.0)
		result14 = self.q1.getRight()
		self.assertEqual(result14,2.0)

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
		self.assertEqual(type(self.q2),Quadrilateral)

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
		result10 = self.sq1.getName()
		self.assertEqual(result10,'Square')

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
		result10 = self.rec1.getName()
		self.assertEqual(result10,'Rectangle')

	def test_I002_test_rectangle_get_set_COM(self):
		result1 = self.rec2.getCOM()
		self.assertEqual(result1,(1.0,1.0))
		self.rec2.setCOM(4.0,4.0)
		result2 = self.rec2.getCOM()
		self.assertEqual(result2,(4.0,4.0))

class TestAutomobileClass(unittest.TestCase):
	def setUp(self):
		self.a1 = Automobile()

	def tearDown(self):
		del self.a1

	def test_J001_test_automobile_creation(self):
		'Test creation of an Automobil object'
		result = self.a1.getAutomobileCount()
		self.assertEqual(result,0)

	def test_J002_test_automobile_get_COM(self):
		'Test the getCOM func of an Automobile Object'
		result = self.a1.getCOM()
		self.assertEqual(result,"Automobile object is returning COM")

class TestCarClass(unittest.TestCase):
	def setUp(self):
		self.car1 = Car(0.0,0.0)
		self.car2 = Car(1.0,1.0)

	def tearDown(self):
		del self.car1
		del self.car2

	def test_K001_test_car_creation(self):
		'Test creation of a Car object'
		result1 = self.car1.getAutomobileCount()
		self.assertEqual(result1,2)
		result2 = self.car1.left()
		self.assertEqual(result2,-4.0)
		result3 = self.car1.right()
		self.assertEqual(result3,4.0)
		result4 = self.car1.top()
		self.assertEqual(result4,2.0)
		result5 = self.car1.bottom()
		self.assertEqual(result5,-1.5)
		result6 = self.car1.getCOM()
		self.assertEqual(result6,(0.0,0.0))
		result7 = self.car1.getAutoNum()
		self.assertEqual(result7,1)
		result8 = self.car1.getAutoName()
		self.assertEqual(result8,'Car')

class TestTruckClass(unittest.TestCase):
	def setUp(self):
		self.truck1 = Truck(0.0,0.0)
		self.truck2 = Truck(1.0,1.0)

	def tearDown(self):
		del self.truck1
		del self.truck2

	def test_L001_test_truck_creation(self):
		'Test creation of a Truck object'
		result1 = self.truck1.getAutomobileCount()
		self.assertEqual(result1,2)
		result2 = self.truck1.left()
		self.assertEqual(result2,-10)
		result3 = self.truck1.right()
		self.assertEqual(result3,15)
		result4 = self.truck1.top()
		self.assertEqual(result4,5)
		result5 = self.truck1.bottom()
		self.assertEqual(result5,-6)
		result6 = self.truck1.getCOM()
		self.assertEqual(result6,(0.0,0.0))
		result7 = self.truck1.getAutoNum()
		self.assertEqual(result7,1)
		result8 = self.truck1.getAutoName()
		self.assertEqual(result8,'Truck')

class TestBusClass(unittest.TestCase):
	def setUp(self):
		self.bus1 = Bus(0.0,0.0)
		self.bus2 = Bus(1.0,1.0)

	def tearDown(self):
		del self.bus1
		del self.bus2

	def test_M001_test_bus_creation(self):
		'Test creation of a Bus object'
		result1 = self.bus1.getAutomobileCount()
		self.assertEqual(result1,2)
		result2 = self.bus1.left()
		self.assertEqual(result2,-10)
		result3 = self.bus1.right()
		self.assertEqual(result3,15)
		result4 = self.bus1.top()
		self.assertEqual(result4,5)
		result5 = self.bus1.bottom()
		self.assertEqual(result5,-6)
		result6 = self.bus1.getCOM()
		self.assertEqual(result6,(0.0,0.0))
		result7 = self.bus1.getAutoNum()
		self.assertEqual(result7,1)
		result8 = self.bus1.getAutoName()
		self.assertEqual(result8,'Bus')

class TestAutoOverlap(unittest.TestCase):
	def setUp(self):
		self.car1 = Car(0.0,0.0)
		self.car2 = Car(0.0,0.0)

	def tearDown(self):
		del self.car1
		del self.car2

	def test_N001_test_maximum_overlap(self):
		'Two cars with a perfect overlap'
		self.result = assignment.autoOverlap(self.car1,self.car2)
		self.assertEqual(self.result,True)

	def test_N002_test_no_overlap(self):
		'Two Cars with no overlap'
		self.car1 = Car(5.5,5.5)
		self.result = assignment.autoOverlap(self.car1,self.car2)
		self.assertEqual(self.result,False)

	def test_N003_test_slight_overlap(self):
		'Two cars with an appreciable overlap'
		self.car1 = Car(1.0,1.0)
		self.result = assignment.autoOverlap(self.car1,self.car2)
		self.assertEqual(self.result,True)

	def test_N004_test_touching(self):
		'The back wheel of car2 is touching the front body of car1'
		self.car2 = Car(7.5,2.5)
		self.result = assignment.autoOverlap(self.car1,self.car2)
		self.assertEqual(self.result,True)

	def test_N005_test_bumper_touch(self):
		'The front body of Car1 is touching the back body of car2'
		self.car2 = Car(8.0,0.0)
		self.result = assignment.autoOverlap(self.car1,self.car2)
		self.assertEqual(self.result,True)

if __name__ == '__main__':
    unittest.main()
