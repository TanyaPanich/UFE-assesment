# You must have imagemagick installed

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
from math import floor


def animate_spectrum(input_filename, output_filename, fps=60, frames=100, interval=20):
    """
    This function makes an animation of an absorption spectrum. The inmput
    is a tab seprated CSV of the format:

    nm  absorption

    where absorption is in the units of cm^2 * 10^20.

    :param input_filename: The source CSV
    :param output_filename: The output animated gif
    :param fps: The frames per second for the gif
    :param frames: The number of frames in the GIF
    :param interval: TODO document interval
    :return: None, but does write the file to the filesystem.
    """
    df = pd.read_csv('data.ndbay.txt', delimiter='\t', names=['nm', 'absorption_cm2_1.0e_20'])
    nm = df['nm'].values
    absorption = df['absorption_cm2_1.0e_20'].values
    fig, ax = plt.subplots()
    ax.set_ylim((absorption.min(), absorption.max()))
    ax.set_xlim((nm.min(), nm.max()))
    line, = ax.plot([], [], lw=2)

    def init():
        line.set_data([], [])
        return (line,)

    def animate(i):
        left_idx = floor(i / frames * absorption.shape[0])
        right_idx = absorption.shape[0] - left_idx
        right_zeros = np.zeros(right_idx)
        left_absorption = absorption[0:left_idx]
        waveform = np.hstack((left_absorption, right_zeros))
        line.set_data(nm, waveform)
        return (line,)

    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=interval, blit=True)
    anim.save(output_filename, writer='imagemagick', fps=fps)


if __name__ == '__main__':
    print('In the animator')
    animate_spectrum('data.ndbay.txt', 'animation2.gif')
