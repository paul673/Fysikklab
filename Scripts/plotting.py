import matplotlib.pyplot as plt
import Scripts
from .funksjoner import *
FORMAT = "png"
from .readtxt import meanData

def plot(_x, _y, _xfast=0, _yfast=0, label=["tittel", "x", "y"], save=False, name= ""):
    plt.figure('y(x)',figsize=(12,6))
    if not isinstance(_xfast, int) and isinstance(_yfast, int):
        plt.plot(_x,_y,_xfast,_yfast,'*', color=(200/255,0/255,100/255), label="numerisk")
        plt.ylim(0, 0.4)
        #pass
    else:
        print("hu")
        plt.plot(_x, _y, color=(200/255,0/255,100/255), label="numerisk")
        plt.ylim(min(_y)- (1/100), max(_y)+ (1/100))
    plt.title(label[0], fontsize=25)
    plt.xlabel(label[1],fontsize=20)
    plt.ylabel(label[2],fontsize=20)
    #plt.ylim(min(_y),max(_y))
    #plt.ylim(0, 0.4)
    plt.grid()
    if save:
        plt.savefig(f"Plot/{name}.{FORMAT}", bbox_inches='tight')
    plt.show()

def plot2(x1, y1, x2, y2,label=["tittel", "x", "y"], save=False, name= ""):
    plt.figure('y(x)',figsize=(12,6))
    plt.plot(x1, y1, color=(200/255,0/255,100/255), label="numerisk")
    #plt.ylim(min(y1) - (y1[0]/10), max(y1)+ (y1[0]/10))
    plt.ylim(0, max(y1) + (np.mean(y1) / 10))
    plt.title(label[0], fontsize=25)
    plt.xlabel(label[1],fontsize=20)
    plt.ylabel(label[2],fontsize=20)
    plt.plot(x2, y2, color=(100/255,0/255,100/255), label="eksperimentelt")
    plt.grid()
    plt.legend()
    if save:
        plt.savefig(f"Plot/{name}.{FORMAT}", bbox_inches='tight')
    plt.show()





class Plot():
    def __init__(self):
        self.t_data, self.x_data, self.y_data = meanData("Data/verdier/")
        self.y_data = self.y_data - (0.408 - 0.258)
        self.v__x = []
        self.v__y = []
        for i, t in enumerate(self.t_data):
            if i > 0:
                self.dt = abs(self.t_data[i-1]-t)
                self.d__x = abs(self.x_data[i-1]-self.x_data[i])
                self.d__y = abs(self.y_data[i - 1] - self.y_data[i])
                self.v__x.append(self.d__x/self.dt)
                self.v__y.append(self.d__y/self.dt)
        self.v__y = np.array([0] + self.v__y)
        self.v__x = np.array([0] + self.v__x)
        self.v_tot = np.sqrt(self.v__y**2+self.v__x**2)

        return

    def all(self, save=False):
        self.y(save=save)
        self.b(save=save)
        self.k(save=save)
        self.v(save=save)
        self.n(save=save)
        self.f(save=save)
        self.x_t(save=save)
        self.v_t(save=save)


    def tegning(self, save=False, name="tegn"):
        plt.figure('y(x)', figsize=(12, 6))
        plt.plot(x, y, color=(75 / 255, 0 / 255, 130 / 255), label="numerisk")
        plt.scatter(xfast,yfast, color=(0,0,0))
        for i in xfast:
            ag = np.linspace(0, 1, num=100)
            plt.plot([i for j in range(100)], ag, color=(0,0,0))
        plt.ylim(0, 0.3)
        #plt.gca().set_aspect('equal', adjustable='box')
        if save:
            plt.savefig(f"Plot/{name}.{FORMAT}", bbox_inches='tight')
        plt.show()

    def y(self, save=False,name="y(x)"):
        plot2(x, y, self.x_data, self.y_data, label=[r"Bane", r"x [m]", r"y(x) [m]"], save=save, name=name)

    def b(self, save=False,name="b(x)"):
        plot(x, grader(b(x)), label=[r"Vinkel", r"x [m]", r"$\beta$(x) [grader]"], save=save, name=name)

    def k(self, save=False,name="k(x)"):
        plot(x, k(x), label=[r"Krumning", r"x [m]", r"$\kappa$(x) [m$^{-1}$]"], save=save, name=name)

    def v(self, save=False,name="v(x)"):
        plot2(x, v(x),self.x_data, self.v_tot, label=[r"Fart", r"x [m]", r"v(x) [ms$^{-1}$]"], save=save, name=name)

    def n(self, save=False,name="N(x)"):
        plot(x, N(x), label=[r"Normalkraft", r"x [m]", r"N(x) [mg]"], save=save, name=name)

    def f(self, save=False,name="f(x)"):
        plot(x, f_N(x), label=["Kraft", r"x [m]", r"$|R_{k}N^{-1}|$ [N]"], save=save, name=name)


    def x_t(self, save=False,name="x(t)"):
        plot2(t_list(), x, self.t_data, self.x_data, label=["x(t)", r"t [s]", r"x(t) [m]"], save=save, name=name)

    def v_t(self,save=False,name="v(t)"):
        plot2(t_list(), v(x),self.t_data, self.v_tot, label=["v(t)", r"t [s]", r"v(t) ms$^{-1}$]"], save=save, name=name)