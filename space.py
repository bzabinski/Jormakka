import numpy as np
from unit import unit

class space:
    def __init__(self, side):
        self._cube = [[[0 for k in range(side)] for j in range(side)] for i in range(side)]
        for a in range(0, side):
            for b in range(0, side):
                for c in range(0, side):
                    self._cube[a][b][c] = unit(a, b, c)
    def getCube(self):
        return self._cube
