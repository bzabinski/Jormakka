from math import sin
from math import cos
from math import e
from math import pi

reynalds = 10 ** 6
rho = 1 / reynalds
beta = (2 * pi) ** 2 * rho

def g(t):
    G = e ** (-t) * t ** 2
    return 0
def d1g(t):
    D1g = -e ** -t * (t - 2) * t
    return 0
def d2g(t):
    D2g = e ** -t * (t ** 2 - 4 * t + 2)
    return 0
def u1(t, x1, x2, x3):
    U1 = e ** (-beta * t) * (sin(2 * pi * x2 + g(t)) + cos(2 * pi * (x3 + g(t)))) - d1g(t)
    return U1
def u2(t, x1, x2, x3):
    U2 = e ** (-beta * t) * (sin(2 * pi * x1 + g(t)) + cos(2 * pi * (x3 + g(t)))) - d1g(t)
    return U2
def u3(t, x1, x2, x3):
    U3 = e ** (-beta * t) * (sin(2 * pi * x1 + g(t)) + cos(2 * pi * (x2 + g(t)))) - d1g(t)
    return U3
def p(t, x1, x2, x3):
    P1 = e ** (-2 * beta * t) * (2 * pi) ** 2 * sin(2 * pi * (x1 + g(t)) * cos(2 * pi * (x2 + g(t))))
    P2 = e ** (-2 * beta * t) * (2 * pi) ** 2 * sin(2 * pi * (x2 + g(t)) * cos(2 * pi * (x3 + g(t))))
    P3 = e ** (-2 * beta * t) * (2 * pi) ** 2 * sin(2 * pi * (x3 + g(t)) * cos(2 * pi * (x1 + g(t))))
    P4 = D2g * (x1 + x2 + x3)
    P = P4 - P1 - P2 - P3
    return P
