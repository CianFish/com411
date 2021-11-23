import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def read_data(file_path):
    temps = []
    with open(file_path) as file:
        next(file)
        for row in file:
            temps.append(float(row.strip()))

    return temps


def run():
    data = read_data("Temps.txt")
    fig, axes = plt.subplot(1,2)
    days = range(1,8)
    axes[0].plot(days, data)
    axes[1].bar(days, data)

    axes[0].set_xlim(min(days), max(days))
    axes[1].set_xlim(min(days), max(days))

    axes[0].set_ylim(min(data), max(data))
    axes[1].set_ylim(min(data), max(data))

    axes[0].set_xlabel("Days")
    axes[1].set_xlabel("Days")
    axes[0].set_ylabel("Temperatures")

    plt.tight_layout()
    plt.show()
run()
