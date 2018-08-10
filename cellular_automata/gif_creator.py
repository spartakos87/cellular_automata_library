import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

import matplotlib.pyplot as plt

class gif_creator:
    def __init__(self,universe,save=False,filename=''):
        """

        :param universe:is a list of numpy arrays
        :param save: False or True to save
        :param filename:
        """
        self.universe = universe
        self.save = save
        self.filename = filename

    def create_fig(self):
        fig, ax = plt.subplots(figsize=(10, 10))
        temp_frame = plt.imshow(self.universe[0], cmap='binary')

        def update(i):
            temp_frame.set_data(self.universe[i])

        anim = FuncAnimation(
            fig, update, interval=100,frames=len(self.universe),repeat=False)
        if self.save:
            anim.save(self.filename+'.gif', fps=10, writer='imagemagick')
        plt.draw()
        plt.show()







