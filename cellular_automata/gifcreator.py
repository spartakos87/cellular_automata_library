from matplotlib.animation import FuncAnimation
from matplotlib import colors
import matplotlib.pyplot as plt


class GifCreator:
    def __init__(self, universe, save=False, filename='', rule=''):
        """

        :param universe:is a list of numpy arrays
        :param save: False or True to save
        :param filename:
        """
        self.universe = universe
        self.save = save
        self.filename = filename
        self.rule = rule

    def create_fig(self):
        fig, ax = plt.subplots(figsize=(10, 10))
        temp_frame = self._create_first_frame()

        # if self.rule == 2:
        #     temp_frame = plt.imshow(self.universe[0], cmap='binary')
        # else:
        #     # In this case we have multi states, so we need more colors
        #     colors_lst = list(colors._colors_full_map.values())
        #     # Remove white and black , need more checked of this
        #     colors_lst = [i for i in colors_lst if i not in [ '#ffffff','#000000']]
        #     colors_lst =  [ '#ffffff','#000000']+colors_lst[:(self.rule[-1]-2)]
        #     cmap = colors.ListedColormap(colors_lst)
        #     temp_frame = plt.imshow(self.universe[0], cmap=cmap)

        def update(i):
            temp_frame.set_data(self.universe[i])

        anim = FuncAnimation(
            fig, update, interval=100, frames=len(self.universe), repeat=False)
        if self.save:
            anim.save(self.filename + '.gif', fps=10, writer='imagemagick')
        plt.draw()
        plt.show()

    def _create_first_frame(self):
        """

        :return:
        """
        if self.rule == 2:
            temp_frame = plt.imshow(self.universe[0], cmap='binary')
        else:
            # In this case we have multi states, so we need more colors
            colors_lst = list(colors._colors_full_map.values())
            # Remove white and black , need more checked of this
            colors_lst = [i for i in colors_lst if i not in ['#ffffff', '#000000']]
            colors_lst = ['#000000', '#ffffff'] + colors_lst[:(self.rule[-1] - 2)]
            cmap = colors.ListedColormap(colors_lst)
            temp_frame = plt.imshow(self.universe[0], cmap=cmap)
        return temp_frame
