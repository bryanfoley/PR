class Shape(object):
    _shapeCount = 0

    def __init__(self):
        pass

    def __del__(self):
        class_name = self.__class__.__name__

    def getShapeCount(self):
        return Shape._shapeCount

    def getCOM(self):
        pass
