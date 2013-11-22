from space import space
from config import *

import sys
from math import ceil
from math import fmod
import matplotlib as mpl
mpl.use('qt4agg')
from mpl_toolkits.mplot3d import Axes3D
#import numpy as np
from numpy import *
import matplotlib.pyplot as plt

#starting dot
x = 5.4301
y = 0.432
z = 2.341
size = 10
tStep = 0.1

pathX = [x]
pathY = [y]
pathZ = [z]

vectorX = []
vectorY = []
vectorZ = []


#torus = space(size)
#cube = torus.getCube()

for t in range(int(sys.argv[1])):
    vX = u1(t * tStep, x, y, z)
    vY = u2(t * tStep, x, y, z)
    vZ = u3(t * tStep, x, y, z)

    vX = round(vX, 9)
    vY = round(vY, 9)
    vZ = round(vZ, 9)

    vectorX.append(vX)
    vectorY.append(vY)
    vectorZ.append(vZ)

    x += (vX * tStep)
    y += (vY * tStep)
    z += (vZ * tStep)

    x = round(x, 9)
    y = round(y, 9)
    z = round(z, 9)


    if(x > 0):
        x = fmod(x, size)
    else:
        x = fmod(x, size)
        x = size + x
    if(y > 0):
        y = fmod(y, size)
    else:
        y = fmod(y, size)
        y = size + y
    if(z > 0):
        z = fmod(z, size)
    else:
        z = fmod(z, size)
        z = size + z
    #if(mod(t, (int(sys.argv[1]) / 1000)) == 0):
    pathX.append(x)
    pathY.append(y)
    pathZ.append(z)

    print([x, y, z])

c = 2
a = 1
"""
u = r_[0:pi:1000j]
v = r_[0:pi:1000j]
#ux, vx = meshgrid(u,v)
xi = (c + a * cos(v)) * cos(u)
yi = (c + a * cos(v)) * sin(u)
zi = a * sin(v)
"""
fig = plt.figure()
#ax = p3.Axes3D(fig)
ax = fig.gca(projection='3d')
ax.scatter(pathX, pathY, pathZ, label='thing')
#ax.scatter(vectorX, vectorY, vectorZ, label='asdf')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
