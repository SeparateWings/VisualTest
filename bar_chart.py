import random
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Patch

def get_data():
    data = [random.random() for _ in range(15)]
    thresholds = [random.randint(1, 5), random.randint(6, 10)]
    labels = ['Cold' if i < thresholds[0] else 'Warm' if i < thresholds[1] else 'Hot' for i in range(15)]
    return labels, data, thresholds

figure, ax = pyplot.subplots()
defined_colors = ['blue', 'orange', 'red']

def update(num):
    ax.clear()
    labels, data, thresholds = get_data()
    colors = [defined_colors[0] if label == 'Cold' else defined_colors[1] if label == 'Warm' else defined_colors[2] for label in labels]
    ax.bar(range(15), data, color=colors)
    legend_labels = ['Cold', 'Warm', 'Hot']
    legend_elements = [Patch(facecolor=defined_colors[legend_labels.index(label)], label=label) for label in legend_labels]
    ax.legend(handles=legend_elements, loc='upper right')
    return ax,

animation = FuncAnimation(figure, update, frames=range(10), repeat=True)

pyplot.show()
