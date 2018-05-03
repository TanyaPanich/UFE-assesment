import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

def sample(data, samples=None):
    if not samples:
        return data
    keep = int(len(data) / samples)
    return [data[i] for i in range(len(data)) if i % keep == 0]

def pairToFloat(lst):
    return [float(x) for x in lst]

def readData(f, samples=None):
    zipped = sample([pairToFloat(x.split()) for x in open(f, "r")], samples)
    return ([x[0] for x in zipped], [x[1] for x in zipped])

def animateFunc(ax, data):
    def _animate(i):
        print(datetime.now().time())
        line, = ax.plot(data[0][:i], data[1][:i])
        return line,
    return _animate

def initFunc(ax, data):
    def _init():
        line,=ax.plot(data[0], data[1])
        return line,
    return _init

def animation(filename, samples=100, durationMs=10000):
    interval = int(durationMs / samples)
    data = readData(filename, samples)
    fig, ax = plt.subplots()
    return FuncAnimation(fig,
                         animateFunc(ax, data),
                         np.arange(1, len(data[0])),
                         init_func=initFunc(ax, data),
                         interval=interval,
                         blit=True)

if __name__ == '__main__':
    anim = animation("./data.ndbay.txt")
    #data = readData("./data.ndbay.txt", 10)
    #fig, ax = plt.subplots()
    #line,=ax.plot(data[0], data[1])
    plt.show()
