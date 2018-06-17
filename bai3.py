import math
def sincos(x):
    y = []
    z = []
    for i in range(len(x)):
        y.append(math.pi / 2 - x[i])
        z.append(math.cos(x[i]) - math.sin(x[i]))
    return y, z