from torus import torus

import sys
from math import *
import matplotlib as mpl
mpl.use('qt4agg')
from mpl_toolkits.mplot3d import Axes3D
#import numpy as np
from numpy import *
import matplotlib.pyplot as plt

#starting dot
def myCalculate(x1, y1, z1):
    x = x1
    y = y1
    z = z1
    tStep = 0.1
    size = 1.0

    myTorus = torus(size)
    myTorus.setMarker(x, y, z)

    for t in range(int(sys.argv[1])):
        vX = dx(x, y, z)
        vY = dy(x, y, z)
        vZ = dz(x, y, z)
        print(vX, vY, vZ)
        x += (vX * tStep)
        y += (vY * tStep)
        z += (vZ * tStep)

        x = round(x, 9)
        y = round(y, 9)
        z = round(z, 9)

        myTorus.setMarker(x, y, z)
        x, y, z = myTorus.getMarker()
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
