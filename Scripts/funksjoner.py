from .cubicspline import *
import numpy as np
g = 9.81
M = 0.031
c = 2/5
y_0 = 0.258
v_0 = 0
t_0 = 0

def v(x):
    return np.sqrt((2*g*(y_0-y))/1+c)

def k(x):
    return (cs(x,2))/(1+cs(x,1)**2)**(3/2)

def a_s(x):
    return v(x)**2 * k(x)

def b(x):
    return np.arctan(cs(x,1))

def grader(rad):
    return rad * (180/(np.pi))

def N(x):
    return M*(g*np.cos(b(x))+a_s(x))

def f(x):
    return (c*M*g*np.sin(b(x)))/(1+c)

def f_N(x):
    return (f(x))/(N(x))

def a(x):
    return -1 * ((g*np.sin(b(x)))/(1+c))

def anerikke(noe):
    xn1 = xn + vxn * dt
    yn1 = y(xn1)
    vn1 = vn + an * dt
    tn1 = (n + 1)*dt
    return 0

def xt(t):
    #dt = dx / v(x)
    t_n = (2 * dx)/ (v(x)-v(x))

    print([(count+1)*dt[count-1] for count, tn in enumerate(dt, 1)])



    print(dx)
    print(len(v(x)))
    print(dt)
def vt(t):



xt(10)



