from numpy import array

class marker:
    def __init__(self):
        self._currentX = -1
        self._currentY = -1
        self._currentZ = -1

        self._pathX = []
        self._pathY = []
        self._pathZ = []
    def getPos(self):
        return self._currentX, self._currentY, self._currentZ

    def updateAll(self, x, y, z):
        self._currentX = x
        self._currentY = y
        self._currentZ = z

        self._pathX.append(self._currentX)
        self._pathY.append(self._currentY)
        self._pathZ.append(self._currentZ)

    def getPath(self):
        return self._pathX, self._pathY, self._pathZ
