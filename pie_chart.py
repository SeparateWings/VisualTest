import random

from matplotlib import pyplot
from matplotlib.animation import FuncAnimation

def get_data():
    i = random.random() / 2
    j = random.random() / 2
    k = 1 - i - j
    return [i, j, k]

figure, ax = pyplot.subplots()
labels = ['hot', 'warm', 'cold']
colors = ['red', 'orange', 'blue']

def update(num):
    ax.clear()
    data = get_data()
    ax.pie(data, labels=labels, colors=colors, startangle=90)
    ax.set_title('Memory Usage: Hot, Warm, and Cold Proportions')
    return ax,

animation = FuncAnimation(figure, update, frames=range(10), repeat=True)

pyplot.show()
