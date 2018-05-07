from os.path import basename
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

def sample(data, samples=None):
    if not samples or samples >= len(data):
        return data
    step = len(data) / samples
    return [data[int(i * step)] for i in range(samples) if int(i * step) < len(data)]

def listToFloatList(lst):
    return [float(x) for x in lst]

def readData(f, samples=None):
    zipped = sample([listToFloatList(x.split()) for x in open(f, "r")], samples)
    return ([x[0] for x in zipped], [x[1] for x in zipped])
#we call it once, it creates and returns _animate(i), which will be running *samples times
def animateFunc(lines, data_sets):
    def _animate(i):
        #print(datetime.now().time())
        #line, = ax.plot(data[0][:i], data[1][:i], lw=2)
        for idx in range(len(lines)):
            #set_data(array of x,array of y)
            lines[idx].set_data(data_sets[idx][0][:i], data_sets[idx][1][:i])
        return lines
    return _animate

# [[1,2], [3,4]] => [1,2,3,4]
def flatten(list_of_lists):
    result = []
    for lst in list_of_lists:
        result += lst
    return result

# handles multiple files
def animation(filenames, samples=100, durationMs=10000, extraDelayMs=4000,
              chartTitle="Your are in hell", xLabel="heat", yLabel="pain"):
    interval = int(durationMs / samples)
    extra_samples = int(extraDelayMs / interval)
    # Read data from all files into list of datasets.
    #[[[x1, ...], [y1, ...]], [[x1, ...], [y1, ...]], ...]
    data_sets = [readData(filename, samples) for filename in filenames]
    # create rendered objects
    fig, ax = plt.subplots()
    # Set axis ranges based on total min/max.
    all_x_axis = flatten([data[0] for data in data_sets])
    all_y_axis = flatten([data[1] for data in data_sets])
    ax.set_xlim((min(all_x_axis), max(all_x_axis)))
    ax.set_ylim((min(all_y_axis), max(all_y_axis)))
    ax.set_title(chartTitle)
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)

    # generate inital lines. - creates empty graph - will be updates every time (samples)
    # data sets - hown many files we have
    lines = [ax.plot([], [], lw=2, label=basename(filename))[0] for filename in filenames]
    ax.legend()

    # start rendering
    return FuncAnimation(fig=fig,
                         func=animateFunc(lines, data_sets),
                         frames=samples+extra_samples,
                         interval=interval,
                         blit=True)

if __name__ == '__main__':
    anim = animation(["./db/ndyag.txt"])
    #data = readData("./data.ndbay.txt", 10)
    #fig, ax = plt.subplots()
    #line,=ax.plot(data[0], data[1])
    plt.show()
