from marker import marker

class space:
    def __init__(self, side):
        self._currentAMarker = marker()
        self._currentBMarker = marker()
        """
        self._cube = [[[0 for k in range(side)] for j in range(side)] for i in range(side)]
        for a in range(0, side):
            for b in range(0, side):
                for c in range(0, side):
                    if a1, b1, c1 == a, b, c
                        self._cube[a][b][c] = unit(a, b, c)
                    else
                        self._cube[a][b][c] = 0
    def getCube(self):
        return self._cube
        """

    def getAMarker(self):
        return self._currentAMarker
    def setAMarker(self, a, b, c):
        self._currentAMarker.updateAll(a, b, c)

    def getBMarker(self):
        return self._currentBMarker
    def setBMarker(self, a, b, c):
        self._currentBMarker.updateAll(a, b, c)

    def getAPath(self):
        return self._currentAMarker.getPath()
    def getBPath(self):
        return self._currentAMarker.getPath()
