import matplotlib.pyplot as plt
import Scripts
from .funksjoner import *
FORMAT = "png"

def plot(_x, _y, _xfast=0, _yfast=0, label=["tittel", "x", "y"], save=False, name= ""):
    baneform = plt.figure('y(x)',figsize=(12,6))
    if not isinstance(_xfast, int) and isinstance(_yfast, int):
        plt.plot(_x,_y,_xfast,_yfast,'*')
        plt.ylim(0, 0.4)
        #pass
    else:
        plt.plot(_x, _y)
        plt.ylim(min(_y)- (_y[0]/10), max(_y)+ (_y[0]/10))
    plt.title(label[0])
    plt.xlabel(label[1],fontsize=20)
    plt.ylabel(label[2],fontsize=20)
    #plt.ylim(min(_y),max(_y))
    #plt.ylim(0, 0.4)
    plt.grid()
    if save:
        plt.savefig(f"Plot/{name}.{FORMAT}", bbox_inches='tight')
    plt.show()





class Plot():
    def __init__(self):
        return

    def all(self, save=False):
        self.y(save=save)
        self.b(save=save)
        self.k(save=save)
        self.v(save=save)
        self.n(save=save)
        self.f(save=save)
        self.xt(save=save)
        self.vt(save=save)


    def y(self, save=False,name="y(x)"):
        plot(x, y, xfast, yfast, label=[r"Bane", r"x [m]", r"y(x) [m]"], save=save, name=name)

    def b(self, save=False,name="b(x)"):
        plot(x, grader(b(x)), label=[r"Vinkel", r"x [m]", r"b(x) [grader]"], save=save, name=name)

    def k(self, save=False,name="k(x)"):
        plot(x, k(x), label=[r"Krumning", r"x [m]", r"k(x) [1/m]"], save=save, name=name)

    def v(self, save=False,name="v(x)"):
        plot(x, v(x), label=[r"Fart", r"x [m]", r"v(x) [m/s]"], save=save, name=name)

    def n(self, save=False,name="N(x)"):
        plot(x, N(x), label=[r"Normalkraft", r"x [m]", r"N(x) [mg]"], save=save, name=name)

    def f(self, save=False,name="f(x)"):
        plot(x, f(x), label=["Kraft", r"x [m]", r"f(x) [N]"], save=save, name=name)


    def xt(self, save=False,name="x(t)"):
        pass

    def vt(self,save=False,name="v(t)"):
        pass