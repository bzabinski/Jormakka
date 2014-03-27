#from math import fmod
from space import space

class torus:
    def __init__(self, side):
        self._side = side
        self._cube = space(side)
    def setMarker(self, a, b, c):
        #self._cube.setMarker(fmod(a, self._side), fmod(b, self._side), fmod(c, self._side))
        self._cube.setMarker(a % self._side, b % self._side, c % self._side)
    def getMarker(self):
        return self._cube.getMarker()
    def getPath(self):
        return self._cube.getPath()
