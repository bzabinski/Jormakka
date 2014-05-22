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
    tStep = 0.01
    size = 100.0

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

        x1 += (vXa * tStep)
        y1 += (vYa * tStep)
        z1 += (vZa * tStep)
        x2 += (vXb * tStep)
        y2 += (vYb * tStep)
        z2 += (vZb * tStep)

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
    print(lyap)
    px1, py1, pz1 = myTorus.getAPath()
    px2, py2, pz2 = myTorus.getBPath()
    return px1, py1, pz1, px2, py2, pz2

startX = -5
startY = 0
startZ = 0
change = 0.00000001
fig = plt.figure()
#ax = p3.Axes3D(fig)
ax = fig.gca(projection='3d')
pathX1, pathY1, pathZ1, pathX2, pathY2, pathZ2 = myCalculate(startX, startY, startZ, startX + change, startY, startZ )
#ax.plot(pathX, pathY, pathZ, label='Rossler')
plt.rc('axes', color_cycle=['r', 'g', 'b', 'y'])
ax.plot(pathX1, pathY1, pathZ1, 'bs', pathX2, pathY2, pathZ2, 'g^')
#ax.plot(pathX2, pathY2, pathZ2, label='thing')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
