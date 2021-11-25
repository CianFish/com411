import matplotlib.pyplot as plt
import csv


def read_data():
    with open('Temps.csv') as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        data = {'week 1': [], 'week 2': []}
        for values in csv_reader:
            data['week 1'].append(values[0])
            data['week 2'].append(values[1])

        return data


def run():
    data = read_data()
    fig, axes = plt.subplots(2, 1, sharex="col")
    days = range(1, 8)

    axes[0].plot(days, data['week 1'])
    axes[1].plot(days, data['week 2'])

    plt.tight_layout()
    plt.show()


run()
