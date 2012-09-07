
from math import pi, cos, sin 
from numpy import arange
from matplotlib import pyplot

class EpicycloidEvolute(object):
    def __init__(self, a=1.0, b=1.0):
        pyplot.clf()
        pyplot.cla()
        self._init(a, b)
    
    def _init(self, a=1.0, b=1.0):
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

    def _draw(self, level=20):
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

    def draw(self, filename=None, level=20):
        self._draw(level)
        if filename:
            pyplot.savefig(filename, format='png')
        else:
            pyplot.show()
    def draw_multi(self, to, filename=None, level=20):
        r = int(round((to-1) ** 0.5))
        if r * r < to -1:
            r += 1
        c = r
        pyplot.figure(figsize=(r*3, r*3))
        for i in range(1, to):
            self._init(a=float(i), b=1.0)
            pyplot.subplot(r, c,  i)
            self._draw(level)
        if filename:
            pyplot.savefig(filename, format='png')
        else:
            pyplot.show()

x = EpicycloidEvolute()
x.draw_multi(17, 'all.png')

#for i in range(1, 16):
#    a = float(i)
#    x = EpicycloidEvolute(a, 1.0)
#    x.draw('ee_%d.png' %(i), level=20)



