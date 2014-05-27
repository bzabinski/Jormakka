from math import fmod
from space import space

class torus:
    def __init__(self, side, a, b, c, d, e, f):
        self._side = side
        self._cube = space(side, a, b, c, d, e, f)
    def setAMarker(self, a, b, c):
        #self._cube.setMarker(fmod(a, self._side), fmod(b, self._side), fmod(c, self._side))
        self._cube.setAMarker(fmod(a, self._side), fmod(b, self._side), fmod(c, self._side))
    def setBMarker(self, a, b, c):
        #self._cube.setMarker(fmod(a, self._side), fmod(b, self._side), fmod(c, self._side))
        self._cube.setBMarker(fmod(a, self._side), fmod(b, self._side), fmod(c, self._side))
    def getAMarker(self):
        return self._cube.getAMarker()
    def getAPath(self):
        return self._cube.getAPath()

    def getBMarker(self):
        return self._cube.getBMarker()
    def getBPath(self):
        return self._cube.getBPath()
