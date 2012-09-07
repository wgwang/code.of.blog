
from math import pi, cos, sin 
from numpy import arange
from matplotlib import pyplot

class EpicycloidEvolute(object):
    def __init__(self, a=1.0, b=8.0):
        self.a = float(a)
        self.b = float(b)
        self.k = a/(a+2*b)
        self.fx = lambda t : (a+b)*cos(t) - b*cos((a/b+1)*t)
        self.fy = lambda t : (a+b)*sin(t) - b*sin((a/b+1)*t)
        self.gx = lambda t : (a+b)*cos(t) + b*cos((a/b+1)*t)
        self.gy = lambda t : (a+b)*sin(t) + b*sin((a/b+1)*t)

    def _epicloid(self, n, t):
        kk = self.k ** n
        if n % 2 == 0:
            xx = kk * self.fx(t)
            yy = kk * self.fy(t)
        else:
            xx = kk * self.gx(t)
            yy = kk * self.gy(t)
        return (xx, yy)

    def draw(self, filename=None, level=20):
        for n in range(level):
            x = []
            y = []
            for t in arange(0, 2*pi+0.1, 0.1):
                xx, yy = self._epicloid(n, t)
                x.append(xx)
                y.append(yy)
            pyplot.plot(x, y)
        pyplot.axis('equal')
        pyplot.axis('off')
        if filename:
            pyplot.savefig(filename, format='png') #, facecolor='black')
        else:
            pyplot.show()
        pyplot.cla()
        pyplot.clf()


for i in range(2, 16):
    a = float(i)
    x = EpicycloidEvolute(a, 1.0)
    x.draw('ee_%d.png' %(i), level=20)



