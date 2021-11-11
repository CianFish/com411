import matplotlib.pyplot as plt
import random

def data():
    paths = {}
    line = str(input("What line would you like? :, -- or -"))
    paths["line"] = line
    colour = str(input("What colour would you like? r,g or b"))
    paths["colour"] = colour
    marker = str(input("What style of marker would you like? o,s or ^"))
    paths["marker"] = marker

    return (paths)

def generate():
    lines = int(input("How many lines would you like to display?"))
    for call in range(lines):
        values = data()
        x = random.sample(range(1,10), 5)
        y = random.sample(range(1,10), 5)
        format = f"{values['colour']}{values['marker']}{values['line']}"
        plt.plot(x,y,format)
    plt.show()

def run():
    print("Running...")
    generate()
    print("Done!")

run()