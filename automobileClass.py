class Automobile(object):
    _automobileCount = 0

    def __init__(self):
        pass

    def __del__(self):
        class_name = self.__class__.__name__

    def getAutomobileCount (self) :
        return Automobile._automobileCount

    def getCOM (self) :
        return "Automobile object is returning COM"