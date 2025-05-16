import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.image as mpimg
import matplotlib as mpl

class SquirrelRenderer:
    def __init__(self,
                 size: float = 6.0,
                 xlim=(0, 6),
                 ylim=(-3, 3),
                 ):
        """
        Initialize the SquirrelRenderer with a specified width and height.
        Args:
            size: Height and width of the figure in inches.
            xlim: x-axis limits, iterable.
            ylim: y-axis limits, iterable.
        """
        squirrel_size = 0.5 # [axis units] 

        # Create a figure and axes.
        self.fig, self.ax = plt.subplots(figsize=(size, size))
        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim)

        # This will make x distances equal to y distances.
        self.ax.set_aspect('equal', adjustable='box')

        # Get our squirrel image.
        self.image = mpimg.imread("images/squirrel.gif")

        # Set the background image.
        self.background = mpimg.imread("images/starfield.jpg")
        self.ax.imshow(self.background, extent=[0, 6, -3, 3], aspect='auto')

        # Set the axis to be invisible.
        self.ax.axis('off')

        # Eliminate the border around the figure.
        self.fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

        # Create empty objects that we will populate later.
        # If we draw them now, they will stay on the screen in their initial
        # positions for the entire animation, so don't populate them.
        self.squirrel = self.ax.imshow([[]],
                                     extent= [-squirrel_size/2,
                                               squirrel_size/2, 
                                              -squirrel_size/2,
                                               squirrel_size/2],
                                     animated=True)
        # Add some friendly red and blue dots.
        self.red, = self.ax.plot([], [], 'ro')
        self.blue, = self.ax.plot([], [], 'bo')

        # Convenient list of objects to be redrawn in each frame.
        self.objects = [self.red, self.blue, self.squirrel]

        # Create the animation object.
        # Interval is the delay between frames in milliseconds (33ms ~= 30fps).
        # Frame values are passed to the update function.
        self.ani = FuncAnimation(self.fig, self.update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=self.init, blit=True, interval=33, repeat=False)

    def init(self):
        """
        Must return an iterable of artists to be redrawn.
        """
        return self.objects

    def draw_squirrel_at(self, x, y):
        """
        Draw the squirrel at the specified x and y coordinates.
        Args:
            x: x coordinate
            y: y coordinate
        """
        # This is somewhat inefficient.
        # TODO: only draw the squirrel once, and then just move it around.
        self.squirrel.set_data(self.image)
        translation = mpl.transforms.Affine2D().translate(x, y)
        self.squirrel.set_transform(translation + self.ax.transData)
        return self.squirrel
    
    def update(self, frame):
        """
        Update the plot for each frame.
        Args:
            frame: The current frame value. This need not be an integer, and
            simply takes on each value of the frame iterable passed to FuncAnimation.
        """
        offset = 3
        self.draw_squirrel_at(np.sin(frame) + offset, np.cos(frame))
        # Draw the friendly dots.
        self.red.set_data([frame], [np.sin(frame)])
        self.blue.set_data([frame], [np.cos(frame)])
        return self.objects

    def run(self):
        """
        Run the animation.
        This is blocking and will not return until the animation is closed!
        """
        plt.show()

if __name__ == "__main__":
    sr = SquirrelRenderer()
    sr.run()