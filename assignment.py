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
    xOverlap = False
    yOverlap = False

    #Check for similar Centre of Mass (COM)
    if (carA.getCOM()==carB.getCOM()):
        xOverlap = True
        yOverlap = True
    #Else move onto the other detection methods
    else:
        #Two Circle objects
        if (carA.getName()=='Circle' and carB.getName()=='Circle'):
            if( doTouch(carA,carB)):
                xOverlap = True
                xOverlap = True

        #Two Square/Rectangle objects
        elif (carA.getName() != 'Circle' and carB.getName != 'Circle'):
            if ( (valueInRange(carA.x(),carB.left(), carB.right())) or 
               ( valueInRange(carB.x(), carA.left(), carA.right()))):
                xOverlap = True
    
            if ( (valueInRange(carA.y(), carB.bottom(), carB.top())) or
               ( valueInRange(carB.y(), carA.bottom(), carA.top()))):
                yOverlap = True
        else:
            #Square/Rectangle object and Circle Object
            xDistance = math.fabs(carA.x() - carB.x())
            yDistance = math.fabs(carA.y() - carB.y())
            
            if (xDistance <= carA.getHalfWidth() + carB.getHalfWidth()):
                xOverlap = True

            if (yDistance <= carA.getHalfHeight() + carB.getHalfHeight()):
                yOverlap = True

    return (xOverlap and yOverlap)

def valueInRange(value, min, max):
    return ((value >= min) and (value <= max))

def sqr(x):
    return x*x

def doTouch(carA,carB):
    result = False
    if ( math.sqrt(sqr(carB.x() - carA.x()) + sqr(carB.y() - carA.y())) <= carA.getHalfWidth() + carB.getHalfWidth()):
        result = True
    return result