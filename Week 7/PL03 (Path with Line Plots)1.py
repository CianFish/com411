import matplotlib.pyplot as plt

def coordinate():
    x = int(input("Enter an X value - "))
    y = int(input("Enter an Y value - "))

    return (x, y)

def path():
    x_values = []
    y_values = []

    for loop in range(4):
        data = coordinate()
        x_values.append(data[0])
        y_values.append(data[1])

    return x_values, y_values

def run():
    values = path()

    plt.xlabel("X values")
    plt.ylabel("Y values")

    plt.plot(values[0], values[1], "ro--")
    plt.show()

run()
