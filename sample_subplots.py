import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

def sample_subplots():
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    fig, ax = plt.subplots(211)
    ax.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

    fig, ax = plt.subplots(212)
    ax.plot(t2, np.cos(2*np.pi*t2), 'r--')

    return fig

def sample_subplots2png():
    fig = sample_subplots()
    bytesIO = BytesIO()
    plt.savefig(bytesIO, dpi=fig.dpi)
    bytesIO.seek(0)
    return bytesIO

if __name__ == '__main__':
    sample_subplots()
    plt.show()
