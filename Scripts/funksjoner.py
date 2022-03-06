from .cubicspline import *
import numpy as np
g = 9.81
M = 0.031
c = 2/5
y_0 = 0.258
v_0 = 0
t_0 = 0

def v(x):
    return np.sqrt((2 * g * (y_0 - y)) / (1 + c))

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



def t_list():
    vxn = v(x) * np.cos(b(x))
    vxnm1 = vxn[:-1]
    vxn = vxn[1:]
    meanvx = 0.5 * (vxnm1 + vxn)
    dt = dx / meanvx
    t_list = []
    t_value = 0
    for count, tn in enumerate(dt):
        t_list.append(t_value)
        t_value += tn
    t_list.append(t_value)
    return np.array(t_list)

def vt(t):
    return 1+1


endSpeed = [0.9266263928568857, 0.9988205512360724, 0.9701802589622793, 1.0124125912987672, 0.9154427311420857, 0.9216622689363054, 1.0104658016088541, 0.9457921282169819, 0.9467878457420039, 0.961692216748455]
def avgEndSpeed():
    speedSum = 0
    for speed in endSpeed:
        speedSum += speed
    return speedSum / len(endSpeed)


def stanDev():
    sum = 0
    for speed in endSpeed:
        sum += (speed - avgEndSpeed())**2
    return np.sqrt(sum/(len(endSpeed)-1))

def stanErr():
    return stanDev()/ np.sqrt(len(endSpeed))








