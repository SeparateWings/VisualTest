from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange

MAX_FRAMES = 10

x_data, y_data = [], []

figure = pyplot.figure()
line, = pyplot.plot(x_data, y_data, '-')

def update(frame):
    x_data.append(datetime.now())
    y_data.append(randrange(0, 100))
    line.set_data(x_data, y_data)
    figure.gca().relim()
    figure.gca().autoscale_view()
    return line,

animation = FuncAnimation(figure, update, interval=200, save_count=MAX_FRAMES)

pyplot.show()
