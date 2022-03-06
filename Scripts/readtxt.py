import numpy as np
import os
import collections


def readfile(filename):
    f = open(filename, "r")
    l = f.read()
    header = """mass_A
t	x	y
"""
    l = l.replace(header,"")
    l = l.replace("Eâˆ’", "e-")
    l = l.replace(",", ".")
    l = l.replace("âˆ’", "-")
    data = l.split("\n")

    for i,s in enumerate(data):
        if s == "":
            data.pop(i)
        else:
            data[i] = s.split("\t")
    t_data = []
    x_data = []
    y_data = []
    for l in data:
        t_data.append(float(l[0]))
        x_data.append(float(l[1]))
        y_data.append(float(l[2]))
    t_data = np.array(t_data)
    x_data = np.array(x_data)
    y_data = np.array(y_data)
    f.close()
    return t_data, x_data, y_data



def getAllData(path):
    lenghtlist = np.array([])
    all_t_data = []
    all_x_data = []
    all_y_data = []
    for filename in os.listdir(path):
        f = os.path.join(path, filename)
        if os.path.isfile(f):
            t_data, x_data, y_data = readfile(f)
            all_t_data.append(t_data)
            all_x_data.append(x_data)
            all_y_data.append(y_data)
            lenghtlist = np.append(lenghtlist,len(t_data))
    return lenghtlist, all_t_data, all_x_data, all_y_data

def meanData(path):
    lenghtlist, all_t_data, all_x_data, all_y_data = getAllData(path)
    maxValue = int(max(lenghtlist))
    minValue = int(min(lenghtlist))
    t_data = np.array([])
    for a in all_t_data:
        if len(t_data) < len(a):
            t_data = a
    for i,a in enumerate(all_x_data):
        diff = int(maxValue) -len(a)
        if diff > 0:
            all_x_data[i] = np.append(a, [0 for j in range(diff)])

    for i,a in enumerate(all_y_data):
        diff = int(maxValue) -len(a)
        if diff > 0:
            all_y_data[i] = np.append(a, [0 for j in range(diff)])

    x_data = sum(all_x_data)
    y_data = sum(all_y_data)
    #print(y_data[-1])
    #print(all_y_data)

    for i in range(minValue):
        x_data[i] = x_data[i]/len(lenghtlist)
        y_data[i] = y_data[i]/len(lenghtlist)


    numberdict = collections.Counter(lenghtlist)
    antall = 0
    for i in range(maxValue, minValue, -1):
        antall += numberdict[i]
        x_data[i-1] = x_data[i-1] / antall
        y_data[i-1] = y_data[i-1] / antall

    return t_data, x_data, y_data









#meanData("../Data/verdier/")