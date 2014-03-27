def lyapCalc(self, marker00, marker01, marker10, marker11):
    self._x00, self._y00, self._z00 = marker00.getPos()
    self._x01, self._y01, self._z01 = marker01.getPos()
    self._x10, self._y10, self._z10 = marker10.getPos()
    self._x11, self._y11, self._z11 = marker11.getPos()
    self._d0 = sqrt(pow(self._x00 - self._x01, 2) + pow(self._y00 - self._y01, 2) + pow(self._z00 - self._z01, 2))
    self._d1 = sqrt(pow(self._x10 - self._x11, 2) + pow(self._y10 - self._y11, 2) + pow(self._z10 - self._z11, 2))
    self._lyap= log2(abs(self._d1/self._d0))
    self._adjustX = self._x01 + self._d0 * (self._x11 - self._x01) / self._d1
    self._adjustY = self._y01 + self._d0 * (self._y11 - self._y01) / self._d1
    self._adjustZ = self._z01 + self._d0 * (self._z11 - self._z01) / self._d1

    return self._adjustX, self._adjustY, self._adjustZ, self._lyap
