a = 0.2
b = 0.2
c = 5.7

def dx(x, y, z):
    DX = -y - z
    return DX
def dy(x, y, z):
    DY = x + a * y
    return DY
def dz(x, y, z):
    DZ = b + z * (x - c)
    return DZ
