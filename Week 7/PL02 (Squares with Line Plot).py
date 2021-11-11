import matplotlib.pyplot as plt

def small():
    x = [3,3,4,4,3]
    y = [3,4,4,3,3]

    plt.plot(x, y, "ro--")

def medium():
    x = [2,2,5,5,2]
    y = [2,5,5,2,2]


    plt.plot(x, y, "go--")


def large():
    x = [1,6, 6]
    y = [6,6 ,1]

    plt.plot(x,y, "bx-")

medium()
small()
large()
plt.show()