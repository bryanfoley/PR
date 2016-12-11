import math

def get_intersections(autos):
    #Ensure that the list is not empty
    try:
        if autos == [] or len(autos)==1:
            raise ValueError
    except ValueError:
        return (['Not enough items in the list! Minimum of 2 required.'])

    results = []
    for autoA in autos:
        for autoB in autos:
            if autoB.getAutoNum() <= autoA.getAutoNum():
                continue
            if (autoOverlap(autoA,autoB)):
                results.append((autoA.getAutoNum(),autoB.getAutoNum()))

    return results

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

def fineOverlap(autoA,autoB):
    result = False
    for a in autoA.components():
        #Check initially for a perfect overlap of COM's
        for b in autoB.components():
            if (COMoverlap(autoA.components()[a],autoB.components()[b])):
                return True
            #Else move onto the other detection methods
            else:      
            #Two Circle objects
                if (autoA.components()[a].getName()=='Circle' and autoB.components()[b].getName()=='Circle'):
                    if (circleXcircle(autoA.components()[a],autoB.components()[b])):
                        return True
        
                #Two Quadrilateral objects
                elif (autoA.components()[a].getName() != 'Circle' and autoB.components()[b].getName() != 'Circle'):
                    if (quadXquad(autoA.components()[a],autoB.components()[b])):
                        return True

                #Quadrilateral object and Circle Object        
                else:
                    if (quadXcircle(autoA.components()[a],autoB.components()[b])):
                        return True

    return result

def autoOverlap(autoA,autoB):
    if (coarseOverlap(autoA,autoB)):
        return (fineOverlap(autoA,autoB))
    else:
        return False