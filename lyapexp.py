from math import *

def lyapCalc(marker00, marker01, marker10, marker11):
    _x00, _y00, _z00 = marker00.getPos()
    _x01, _y01, _z01 = marker01.getPos()
    _x10, _y10, _z10 = marker10
    _x11, _y11, _z11 = marker11
    _d0 = pow(10, -8)
    _d1 = sqrt(pow(_x10 - _x11, 2) + pow(_y10 - _y11, 2) + pow(_z10 - _z11, 2))
    _lyap= log(_d1/_d0)
    _adjustX = _x10 + _d0 * (_x10 - _x11) / _d1
    _adjustY = _y10 + _d0 * (_y10 - _y11) / _d1
    _adjustZ = _z10 + _d0 * (_z10 - _z11) / _d1
    return _adjustX, _adjustY, _adjustZ, _lyap
