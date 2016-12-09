import math

def get_intersections(cars):
    results = []
    for carA in cars:
        for carB in cars:
            if carB.getShapeNum() <= carA.getShapeNum():
                continue
            if (carOverlap(carA,carB)):
                results.append((carA.getShapeNum(),carB.getShapeNum()))

    return results

def carOverlap(carA,carB):
    
    #Check for similar Centre of Mass (COM)
    if (carA.getCOM()==carB.getCOM()):
        return True
    #Else move onto the other detection methods
    else:      
        #Two Circle objects
        if (carA.getName()=='Circle' and carB.getName()=='Circle'):
            return (circleXcircle(carA,carB))
        
        #Two Quadrilateral objects
        elif (carA.getName() != 'Circle' and carB.getName != 'Circle'):
            return (quadXquad(carA,carB))

        #Quadrilateral object and Circle Object        
        else:
            return (quadXcircle(carA,carB))

def valueInRange(value, min, max):
    return ((value >= min) and (value <= max))

def sqr(x):
    return x*x

def circleXcircle(carA,carB):
    return ( math.sqrt(sqr(carB.x() - carA.x()) + sqr(carB.y() - carA.y())) \
             <= carA.getHalfWidth() + carB.getHalfWidth() )

def quadXquad(carA,carB):
    xOverlap = ((valueInRange(carA.x(),carB.left(), carB.right())) or 
               ( valueInRange(carB.x(), carA.left(), carA.right())))
    
    yOverlap = ( (valueInRange(carA.y(), carB.bottom(), carB.top())) or
               ( valueInRange(carB.y(), carA.bottom(), carA.top())))

    return(xOverlap and yOverlap)

def quadXcircle(carA,carB):
    xDistance = math.fabs(carA.x() - carB.x())
    yDistance = math.fabs(carA.y() - carB.y())
            
    xOverlap = (xDistance <= carA.getHalfWidth() + carB.getHalfWidth())

    yOverlap = (yDistance <= carA.getHalfHeight() + carB.getHalfHeight())

    return (xOverlap and yOverlap)