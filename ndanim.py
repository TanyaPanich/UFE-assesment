import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML, Image
from math import floor

fps = 60

df = pd.read_csv('data.ndbay.txt', delimiter='\t', names=['nm', 'absorption_cm2_1.0e_20'])
nm = df['nm'].values
absorption = df['absorption_cm2_1.0e_20'].values

# equivalent to rcParams['animation.html'] = 'html5'
rc('animation', html='html5')

fig, ax = plt.subplots()

ax.set_ylim((absorption.min(), absorption.max()))
ax.set_xlim((nm.min(), nm.max()))

line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return (line,)

def animate(i):
    frame = (nm.max() - nm.min() / fps * 1) - nm.max()
    adj_frame = frame if frame >= 0 else 0
    waveform = np.hstack((absorption[0:adj_frame], np.zeros(absorption.shape[0] - adj_frame)))
    line.set_data(nm, waveform)
    return (line,)

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)

anim.save('animation.gif', writer='imagemagick', fps=fps)
