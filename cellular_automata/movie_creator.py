import matplotlib
# matplotlib.use("Agg")
# import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import matplotlib.pyplot as plt
from matplotlib import colors


class movie_creator:
    def __init__(self,universe,save=True,filename='',rule=''):
        """

        :param universe:is a list of numpy arrays
        :param save: False or True to save
        :param filename:
        """
        self.universe = universe
        self.save = save
        self.filename = filename
        self.rule = rule

    def create_movie(self):
        FFMpegWriter = manimation.writers['ffmpeg']
        metadata = dict(title='Movie Test', artist='Matplotlib',
                        comment='Movie support!')
        writer = FFMpegWriter(fps=15, metadata=metadata)
        fig = plt.figure()
        if self.rule == 2:
            temp = plt.imshow(self.universe[0],cmap='binary')
        else:
            # In this case we have multi states, so we need more colors
            colors_lst = list(colors._colors_full_map.values())
            # Remove white and black , need more checked of this
            colors_lst = [i for i in colors_lst if i not in [ '#ffffff','#000000']]
            colors_lst =  [ '#000000','#ffffff']+colors_lst[:(self.rule[-1]-2)]
            cmap = colors.ListedColormap(colors_lst)
            temp = plt.imshow(self.universe[0],cmap='binary')

        with writer.saving(fig, self.filename+".mp4", len(self.universe)):
            for frame in range(len(self.universe)):
                temp.set_data(self.universe[frame])
                writer.grab_frame()




