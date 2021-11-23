import csv


def temps(file_path):
    temp = []
    g = []
    s = []
    b = []
    n = []
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        temp.append(csv_reader)
        heading = next(csv_reader)
        for values in csv_reader:
            if values[14] == "Gold":
                g.append("i")
            elif values[14] == "Silver":
                s.append("I")
            elif values[14] == "Bronze":
                b.append("a")
            elif values[14] == "NA":
                n.append("A")
            mi = min(values[9])
            ma = max(values[9])
        print(f"There were {len(g)} gold medals altogether between {mi} and {ma}")
        print(f"There were {len(s)} silver medals altogether")
        print(f"There were {len(b)} bronze medals altogether")

def run():
    temps("athlete.csv")


if __name__ == "__main__":
    run()