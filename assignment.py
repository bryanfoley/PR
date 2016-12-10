import math

def get_intersections(autos):
    #Ensure that the list is not empty
    try:
        if autos == []:
            raise ValueError
    except ValueError:
        print('The input list cannot be empty!')
        exit()

    results = []
    for autoA in autos:
        for autoB in autos:
            if autoB.getShapeNum() <= autoA.getShapeNum():
                continue
            if (autoOverlap(autoA,autoB)):
                results.append((autoA.getShapeNum(),autoB.getShapeNum()))

    return results

def autoOverlap(AutoA,AutoB):

    #Check for similar Centre of Mass (COM)
    if (COMoverlap(AutoA,AutoB)):
        return True
    #Else move onto the other detection methods
    else:      
        #Two Circle objects
        if (AutoA.getName()=='Circle' and AutoB.getName()=='Circle'):
            return (circleXcircle(AutoA,AutoB))
        
        #Two Quadrilateral objects
        elif (AutoA.getName() != 'Circle' and AutoB.getName != 'Circle'):
            return (quadXquad(AutoA,AutoB))

        #Quadrilateral object and Circle Object        
        else:
            return (quadXcircle(AutoA,AutoB))

def coarseOverlap(autoA,autoB):
    if(COMoverlap(autoA,autoB)==True):
        return True
    else:
        return (quadXquad(autoA,autoB))

def sqr(x):
    return x*x

def COMoverlap(shapeA,shapeB):
    return (shapeA.getCOM()==shapeB.getCOM())

def circleXcircle(shapeA,shapeB):
    return ( math.sqrt(sqr(shapeB.x() - shapeA.x()) + sqr(shapeB.y() - shapeA.y())) \
             <= shapeA.getHalfWidth() + shapeB.getHalfWidth() )

def quadXquad(shapeA,shapeB):
    xOverlap = ((valueInRange(shapeA.left(), shapeB.left(), shapeB.right())) or 
                (valueInRange(shapeA.right(),shapeB.left(), shapeB.right())) or
                (valueInRange(shapeB.left(), shapeA.left(), shapeA.right())) or
                (valueInRange(shapeB.right(), shapeA.left(), shapeA.right())) )
    
    yOverlap = ((valueInRange(shapeA.top(), shapeB.bottom(), shapeB.top())) or
                (valueInRange(shapeA.bottom(), shapeB.bottom(), shapeB.top())) or
                (valueInRange(shapeB.top(), shapeA.bottom(), shapeA.top())) or
               (valueInRange(shapeB.bottom(), shapeA.bottom(), shapeA.top())) )

    return(xOverlap and yOverlap)

def quadXcircle(shapeA,shapeB):
    xDistance = math.fabs(shapeA.x() - shapeB.x())
    yDistance = math.fabs(shapeA.y() - shapeB.y())
            
    xOverlap = (xDistance <= shapeA.getHalfWidth() + shapeB.getHalfWidth())
    yOverlap = (yDistance <= shapeA.getHalfHeight() + shapeB.getHalfHeight())

    return (xOverlap and yOverlap)

def valueInRange(value, min, max):
    return ((value >= min) and (value <= max))

def coarseOverlap(autoA,autoB):
    if(COMoverlap(autoA,autoB)==True):
        return True
    else:
        return (quadXquad(autoA,autoB))