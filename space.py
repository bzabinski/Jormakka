from marker import marker

class space:
    def __init__(self, side):
        self._currentMarker = marker()
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
    def getMarker(self):
        return self._currentMarker.getPos()
    def setMarker(self, a, b, c):
        self._currentMarker.updateAll(a, b, c)
    def getPath(self):
        return self._currentMarker.getPath()
