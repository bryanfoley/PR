import sys

sys.path.append('../')
import assignment
from carClass import Car
from truckClass import Truck
from busClass import Bus

def main():
    print('Driver code that will test the whole component.')
    print('All tests must be OK before a branch can be merged with Master!!')
    print('This component test will create multi-body objects and test for expected behaviour/results')
    print('-'*40)

    #Flag to determine if we are reay for integration
    #Default is True -> Assume everything is OK, but flag the first failure
    global overallResult
    overallResult=True
    
    #The results will be a list of tuples of the Automobiles that are colliding/intersecting
    #Each Automobile has a unique Automobile number (of type int) to identify it.
    #The tuples will consist of the Automobile number of the colliding Automobiles
    #The final test case will return a list with an error string

    #Run tests
    r1=TEST001()
    r2=TEST002()
    r3=TEST003()
    r4=TEST004()
    
    print('-'*40)

    #Ready for Integration?
    if(overallResult):
        print('READY FOR INTEGRATION')
    else:
        print('NOT READY FOR INTEGRATION!!!!')

def TEST001():
    #TEST001: All shapes have the same Centre of Mass (COM) -> All shapes have overlap
    print('-'*40)
    #List to store automobiles
    autos = []

    #Create Multi-component objects
    car1 = Car(0.0,0.0)
    bus1 = Bus(0.0,0.0)
    truck1 = Truck(0.0,0.0)

    #Append the automobiles to the input list 
    autos.append(car1)
    autos.append(bus1)
    autos.append(truck1)

    #Send the list of automobiles as input to the new method of detecting collisons.
    result = assignment.get_intersections(autos)

    #Clean Up
    del car1
    del bus1
    del truck1

    expected_result = [(1,2),(1,3),(2,3)]
    if(result ==  expected_result):
        print("A perfect overlap of COM's is detected: TEST001 Result is OK!!")
    else:
        print("Expected collisions are not found!! TEST001 Result is NOK!!")
        print("Expected: ",expected_result)
        print("Attained: ",result)
        global overallResult
        overallResult = False

def TEST002():
    #TEST002: All shapes have different Centre of Mass (COM) with no overlap -> No overlap
    print('-'*40)
    #List to store automobiles
    autos = []

    #Create Multi-component objects
    car1 = Car(0.0,0.0)
    bus1 = Bus(10.0,10.0)
    truck1 = Truck(-20.0,17.3)

    #Append the automobiles to the input list 
    autos.append(car1)
    autos.append(bus1)
    autos.append(truck1)

    #Send the list of automobiles as input to the new method of detecting collisons.
    result = assignment.get_intersections(autos)

    #Clean Up
    del car1
    del bus1
    del truck1

    expected_result = []
    if(result ==  expected_result):
        print("No Overlap of any Automobiles detected: TEST002 Result is OK!!")
    else:
        print("Expected collisions are not found!! TEST002 Result is NOK!!")
        print("Expected: ",expected_result)
        print("Attained: ",result)
        global overallResult
        overallResult = False

def TEST003():
        #TEST003: A line of automobiles are touching, bumber to bumber 
    #         -> Expect overlap with at least one other automobiles, each
    #         Some will have an overlap with two automobiles 
    print('-'*40)
    #List to store automobiles
    autos = []

    #Create Multi-component objects
    car1 = Car(0.0,1.5)
    bus1 = Bus(14.0,6.0)
    car2 = Car(33,1.5)
    truck1 = Truck(47,6.0)

    #Append the automobiles to the input list 
    autos.append(car1)
    autos.append(bus1)
    autos.append(car2)
    autos.append(truck1)

    #Send the list of automobiles as input to the new method of detecting collisons.
    result = assignment.get_intersections(autos)

    #Clean Up
    del car1
    del bus1 
    del car2
    del truck1

    expected_result = [(1,2),(2,3),(3,4)]
    if(result ==  expected_result):
        print("Expected collisions are found!! TEST003 Result is OK!!")
    else:
        print("Expected collisions are not found!! TEST003 Result is NOK!!")
        print("Expected: ",expected_result)
        print("Attained: ",result)
        global overallResult
        overallResult = False

def TEST004():
        #TEST004: An empty list is passed in -> get_intersections() returns a list with the string 'Empty list!'
    print('-'*40)
    #List to store cars (shape objects)
    autos=[]

    #Send the list an empty list.
    #The function 'get_intersections()' will print a message to screen and exit
    result = assignment.get_intersections(autos)

    expected_result = ['Empty list!']
    if(result ==  expected_result):
        print('Expected behaviour detected: TEST004 is OK!')
    else:
        print('Incorrect behaviour for an empty list! TEST004 is NOK!!')
        print("Expected: ",expected_result)
        print("Attained: ",result)
        global overallResult
        overallResult = False


if __name__ == '__main__':
    main()