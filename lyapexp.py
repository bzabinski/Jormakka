from torus import torus

import sys
from math import *
import matplotlib as mpl
mpl.use('qt4agg')
from mpl_toolkits.mplot3d import Axes3D
#import numpy as np
from numpy import *
import matplotlib.pyplot as plt

def lyapCalc(self, marker1, marker2):
    self._x1, self._y1, self._z1 = marker1.getPos()
    self._x2, self._y2, self._z2 = marker2.getPos()
    self._d0 = sqrt(pow(orbit1[0][0] - orbit2[0][0], 2) + pow(orbit1[0][1] - orbit2[0][1], 2) + pow(orbit1[0][2] - orbit2[0][2]), 2)
    self._lyapexps = []
    for itr in range(len(orbit1) - 2):
        self._d1 = sqrt(pow(orbit1[itr + 1][0] - orbit2[itr + 1][0], 2) + pow(orbit1[itr + 1][1] - orbit2[itr + 1][1], 2) + pow(orbit1[itr + 1][2] - orbit2[itr + 1][2]), 2)
        self.lyap[itr]= log2(abs(self._d1/self._d0))


    return myTorus.getPath()

fig = plt.figure()
#ax = p3.Axes3D(fig)
ax = fig.gca(projection='3d')
pathX1, pathY1, pathZ1 = myCalculate(0.1, 0.1, 0.5)
pathX2, pathY2, pathZ2 = myCalculate(0.10000001, 0.1, 0.5)
#ax.plot(pathX, pathY, pathZ, label='Rossler')
plt.rc('axes', color_cycle=['r', 'g', 'b', 'y'])
ax.plot(pathX1, pathY1, pathZ1, label='asdf')
ax.plot(pathX2, pathY2, pathZ2, label='thing')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
