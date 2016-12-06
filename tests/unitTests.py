import unittest
import sys

sys.path.append('../')
import assignment

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

if __name__ == '__main__':
    unittest.main()