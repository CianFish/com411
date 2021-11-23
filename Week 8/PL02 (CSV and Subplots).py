import csv
import matplotlib.pyplot as plt


def read_data():
    with open('Temps.csv') as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        data = {'week1': [], 'week2': []}
        for col in csv_reader:
            data['week1'].append(col[0])
            data['week2'].append(col[1])

    return data

def run():
    data = read_data()
    days = range(1,8)

    fig, axes = plt.subplots(2,1)

    axes[0].plot(days, data['week1'])
    axes[1].plot(days, data['week2'])

    axes[0,0].set_xlim(1,7)
    axes[0,0].set_ylim(0, 20)

    axes[0, 1].set_xlim(1, 7)
    axes[0, 1].set_ylim(0, 25)

    axes[0, 1].set_xlabel("Number of days")
    axes[0, 0].set_xlabel("Number of days")
    axes[0, 1].set_ylabel("Temperatures")
    axes[0, 0].set_ylabel("Temperatures")

    plt.tight_layout()
    plt.show()

run()
