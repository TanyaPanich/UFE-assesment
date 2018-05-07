import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

def sample_plot():
    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)
    fig, ax = plt.subplots()
    ax.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    ax.set_title('Sample plot')
    ax.set_xlabel('random x')
    ax.set_ylabel('random y')
    return fig

def sample_plot2png():
    fig = sample_plot()
    bytesIO = BytesIO()
    plt.savefig(bytesIO, dpi=fig.dpi)
    bytesIO.seek(0)
    return bytesIO

if __name__ == '__main__':
    sample_plot()
    plt.show()
