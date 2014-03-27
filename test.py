from torus import torus
from rossler_config import *
from lyapexp import lyapCalc

import sys
from math import *
import matplotlib as mpl
mpl.use('qt4agg')
from mpl_toolkits.mplot3d import Axes3D
#import numpy as np
from numpy import *
import matplotlib.pyplot as plt

#starting dot
def myCalculate(x1, y1, z1, x2, y2, z2):
    tStep = 0.1
    size = 1.0

    myTorus = torus(size)
    myTorus.setAMarker(x1, y1, z1)
    myTorus.setBMarker(x2, y2, z2)

    for t in range(int(sys.argv[1])):
        vXa = dx(x1, y1, z1)
        vYa = dy(x1, y1, z1)
        vZa = dz(x1, y1, z1)
        vXb = dx(x2, y2, z2)
        vYb = dy(x2, y2, z2)
        vZb = dz(x2, y2, z2)

        x1 += (vX1 * tStep)
        y1 += (vY1 * tStep)
        z1 += (vZ1 * tStep)
        x2 += (vX2 * tStep)
        y2 += (vY2 * tStep)
        z2 += (vZ2 * tStep)

        x1 = round(x1, 9)
        y1 = round(y1, 9)
        z1 = round(z1, 9)
        x2 = round(x2, 9)
        y2 = round(y2, 9)
        z2 = round(z2, 9)

        d00 = myTorus.getAMarker()
        d01 = myTorus.getBMarker()
        d10 = [x1, y1, z1]
        d11 = [x2, y2, z2]
        adjustA, adjustB, adjustC, lyap = lyapCalc(d00, d01, d10, d11)

        myTorus.setAMarker(x1, y1, z1)
        myTorus.setBMarker(adjustA, adjustB, adjustC)
    return myTorus.getAPath(), myTorus.getBPath()

startX = 0.1
startY = 0.1
startZ = 0.5
change = 0.00000001
fig = plt.figure()
#ax = p3.Axes3D(fig)
ax = fig.gca(projection='3d')
pathX1, pathY1, pathZ1, pathX2, pathY2, pathZ2 = myCalculate(startX, startY, startZ, startX + change, startY, startZ )
#ax.plot(pathX, pathY, pathZ, label='Rossler')
plt.rc('axes', color_cycle=['r', 'g', 'b', 'y'])
ax.scatter(pathX1, pathY1, pathZ1, label='asdf')
ax.scatter(pathX2, pathY2, pathZ2, label='thing')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
