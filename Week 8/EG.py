import matplotlib.pyplot as plt
import csv


def read_data(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)

        headings = next(csv_reader)
        data = {'week1': [], 'week2': []}

        for values in csv_reader:
            data['week1'].append(values[0])
            data['week2'].append(values[1])

    return data


def run():
    data = read_data('temps.csv')

    fig, axs = plt.subplots(2, 1, sharex="col")

    days = range(1, 8)

    axs[0].plot(days, data['week1'])
    axs[1].plot(days, data['week2'])

    plt.tight_layout()
    plt.show()


run()