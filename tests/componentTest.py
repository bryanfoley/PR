import sys

sys.path.append('../')
import assignment
from circleClass import Circle
from squareClass import Square
from rectangleClass import Rectangle

def main():
    print('Driver code that will test the whole component.')
    
    #Create a list to store the cars
    #The results will be a list of tuples of the shapes (read as cars) that are colliding/intersecting
    #Each shape has a unique shape number (of type int) to identify it.
    #The tuples will consist of the shape number of the colliding shapes
    
    #TEST001: All shapes have the same Centre of Mass (COM) -> All shapes have overlap

    #List to store cars (shape objects)
    cars = []

    #Create Single Component Shapes to act as cars
    c1 = Circle(1.0,1.0,1.0)
    c2 = Circle(1.0,1.0,1.0)
    sq1 = Square(1.0,1.0,2.0)
    rec1 = Rectangle(1.0,1.0,3.0,2.0)

    #Append the cars to the input list 
    cars.append(c1)
    cars.append(c2)
    cars.append(sq1)
    cars.append(rec1)

    #Send the list of cars as input to the new method of detecting collisons.
    #The results will be a list of tuples of the shapes (read as cars) that are colliding/intersecting
    #Each shape has a unique shape number (of type int) to identify it.
    #The tuples will consist of the shape number of the colliding shapes
    result = assignment.get_intersections(cars)

    expected_result = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
    if(result ==  expected_result):
        print("Expected collisions are found!! TEST001 Result is OK!!")
    else:
        print("Expected collisions are not found!! TEST001 Result is NOK!!")
        print("Expected: ",expected_result)
        print("Attained: ",result)

    del c1
    del c2
    del sq1
    del rec1

    #TEST002: All shapes have different Centre of Mass (COM) with no overlap -> No overlap

    #List to store cars (shape objects)
    cars = []

    #Create Single Component Shapes to act as cars
    c1 = Circle(10.0,10.0,1.0)
    c2 = Circle(-10.0,-10.0,3.0)
    sq1 = Square(0.0,10.0,2.0)
    rec1 = Rectangle(0.0,-10.0,3.0,2.0)

    #Append the cars to the input list 
    cars.append(c1)
    cars.append(c2)
    cars.append(sq1)
    cars.append(rec1)

    #Send the list of cars as input to the new method of detecting collisons.
    #The results will be a list of tuples of the shapes (read as cars) that are colliding/intersecting
    #Each shape has a unique shape number (of type int) to identify it.
    #The tuples will consist of the shape number of the colliding shapes
    result = assignment.get_intersections(cars)

    expected_result = []
    if(result ==  expected_result):
        print("Expected collisions are found!! TEST002 Result is OK!!")
    else:
        print("Expected collisions are not found!! TEST002 Result is NOK!!")
        print("Expected: ",expected_result)
        print("Attained: ",result)

    del c1
    del c2
    del sq1
    del rec1

    #TEST003: Four Unit Circles are located around a Unit Square centred at (0.0,0.0) -> Overalp of Square with each circle 

    #List to store cars (shape objects)
    cars = []

    #Create Single Component Shapes to act as cars
    c1 = Circle(-1.5,0.0,1.0)
    c2 = Circle(0.0,1.5,1.0)
    c3 = Circle(1.5,0.0,1.0)
    c4 = Circle(0.0,-1.5,1.0)
    sq1 = Square(0.0,0.0,1.0)

    #Append the cars to the input list 
    cars.append(c1)
    cars.append(c2)
    cars.append(c3)
    cars.append(c4)
    cars.append(sq1)

    #Send the list of cars as input to the new method of detecting collisons.
    #The results will be a list of tuples of the shapes (read as cars) that are colliding/intersecting
    #Each shape has a unique shape number (of type int) to identify it.
    #The tuples will consist of the shape number of the colliding shapes
    result = assignment.get_intersections(cars)

    expected_result = [(1,5),(2,5),(3,5),(4,5)]
    if(result ==  expected_result):
        print("Expected collisions are found!! TEST003 Result is OK!!")
    else:
        print("Expected collisions are not found!! TEST003 Result is NOK!!")
        print("Expected: ",expected_result)
        print("Attained: ",result)

    del c1
    del c2 
    del c3
    del c4
    del sq1

    #TEST004: A unit circle is just touching the top right vertex of a Unit Square -> Overalp of Square with Circle 

    #List to store cars (shape objects)
    cars = []

    #Create Single Component Shapes to act as cars
    c1 = Circle(1.5,1.5,1.0)
    sq1 = Square(0.0,0.0,1.0)

    #Append the cars to the input list 
    cars.append(c1)
    cars.append(sq1)

    #Send the list of cars as input to the new method of detecting collisons.
    #The results will be a list of tuples of the shapes (read as cars) that are colliding/intersecting
    #Each shape has a unique shape number (of type int) to identify it.
    #The tuples will consist of the shape number of the colliding shapes
    result = assignment.get_intersections(cars)

    expected_result = [(1,2)]
    if(result ==  expected_result):
        print("Expected collisions are found!! TEST004 Result is OK!!")
    else:
        print("Expected collisions are not found!! TEST004 Result is NOK!!")
        print("Expected: ",expected_result)
        print("Attained: ",result)

    del c1
    del sq1

if __name__ == '__main__':
    main()
