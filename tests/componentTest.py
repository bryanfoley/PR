import sys

sys.path.append('../')
import assignment

def main():
    print('Driver code that will test the whole component.')

    results = []
    cars_x = [1.0,2.0,3.0,4.0,5.0]
    cars_y = [2.0,4.0,6.0,8.0,10.0]
    cars_width = [1.0,1.0,1.0,1.0,1.0]
    cars_height = [1.0,1.0,1.0,1.0,1.0]
    cars_is_circular = True

    results = assignment.get_intersections(cars_x,cars_y,cars_width,cars_height,cars_is_circular)

    print('Overlap detected in the following cars:')
    print(results)
    if(results==[]):
        print('No overlap detected, Result is OK!')
    else:
        print('The incorrect overlap was detected! NOK!')

    cars_x = [1.0,2.0,3.0,4.0,5.0]
    cars_y = [1.0,1.0,3.0,4.0,5.0]
    cars_width = [1.5,1.0,1.0,1.0,1.0]
    cars_height = [1.5,1.0,1.0,1.0,1.0]
    cars_is_circular = True

    results = assignment.get_intersections(cars_x,cars_y,cars_width,cars_height,cars_is_circular)

    print('Overlap detected in the following cars:')
    print(results)
    if(results==[(0,1)]):
        print('One Overlap detected, Result is OK!')
    else:
        print('The incorrect overlap was detected! NOK!')

if __name__ == '__main__':
    main()