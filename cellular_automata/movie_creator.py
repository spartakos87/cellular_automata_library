import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import matplotlib.pyplot as plt

class movie_creator:
    def __init__(self,universe,save=True,filename=''):
        """

        :param universe:is a list of numpy arrays
        :param save: False or True to save
        :param filename:
        """
        self.universe = universe
        self.save = save
        self.filename = filename

    def create_movie(self):
        FFMpegWriter = manimation.writers['ffmpeg']
        metadata = dict(title='Movie Test', artist='Matplotlib',
                        comment='Movie support!')
        writer = FFMpegWriter(fps=15, metadata=metadata)
        fig = plt.figure()
        temp = plt.imshow(self.universe[0],cmap='binary')
        with writer.saving(fig, self.filename+".mp4", len(self.universe)):
            for frame in range(len(self.universe)):
                temp.set_data(self.universe[frame])
                writer.grab_frame()




