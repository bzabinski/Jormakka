from space import space
from rossler_config import *

import sys
from math import *
import matplotlib as mpl
mpl.use('qt4agg')
from mpl_toolkits.mplot3d import Axes3D
#import numpy as np
from numpy import *
import matplotlib.pyplot as plt

#starting dot
x = -5
y = 0
z = 0
tStep = 0.01

pathX = [x]
pathY = [y]
pathZ = [z]

vectorX = []
vectorY = []
vectorZ = []


#torus = space(size)
#cube = torus.getCube()

for t in range(int(sys.argv[1])):
    vX = dx(x, y, z)
    vY = dy(x, y, z)
    vZ = dz(x, y, z)

    x += (vX * tStep)
    y += (vY * tStep)
    z += (vZ * tStep)

    x = round(x, 9)
    y = round(y, 9)
    z = round(z, 9)

    pathX.append(x)
    pathY.append(y)
    pathZ.append(z)

    print([x, y, z])

fig = plt.figure()
#ax = p3.Axes3D(fig)
ax = fig.gca(projection='3d')
ax.plot(pathX, pathY, pathZ, label='Rossler')
#ax.scatter(vectorX, vectorY, vectorZ, label='asdf')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
