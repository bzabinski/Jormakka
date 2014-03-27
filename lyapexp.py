def lyapCalc(marker00, marker01, marker10, marker11):
    _x00, _y00, _z00 = marker00.getPos()
    _x01, _y01, _z01 = marker01.getPos()
    _x10, _y10, _z10 = marker10.getPos()
    _x11, _y11, _z11 = marker11.getPos()
    _d0 = sqrt(pow(_x00 - _x01, 2) + pow(_y00 - _y01, 2) + pow(_z00 - _z01, 2))
    _d1 = sqrt(pow(_x10 - _x11, 2) + pow(_y10 - _y11, 2) + pow(_z10 - _z11, 2))
    _lyap= log2(abs(_d1/_d0))
    _adjustX = _x01 + _d0 * (_x11 - _x01) / _d1
    _adjustY = _y01 + _d0 * (_y11 - _y01) / _d1
    _adjustZ = _z01 + _d0 * (_z11 - _z01) / _d1

    return self._adjustX, self._adjustY, self._adjustZ, self._lyap
