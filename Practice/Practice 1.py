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
            mi = values[9]

            if values[14] == "Gold":
                g.append("i")
            elif values[14] == "Silver":
                s.append("I")
            elif values[14] == "Bronze":
                b.append("a")
            elif values[14] == "NA":
                n.append("A")

    return g, s, b

def minimum(file_path):
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        mi = 2022
        for row in csv_reader:
            if int(row[9]) < mi:
                mi = int(row[9])

    return mi

def maximum(file_path):
        with open(file_path) as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            ma = 1900
            for row in csv_reader:
                if int(row[9]) > ma:
                    ma = int(row[9])
        return ma

def run():
    a = temps("athlete.csv")
    mb = minimum("athlete.csv")
    mc = maximum("athlete.csv")

    print(f"There were {len(a[0])} gold medals altogether between {mb} and {mc}")
    print(f"There were {len(a[1])} silver medals altogether between {mb} and {mc}")
    print(f"There were {len(a[2])} bronze medals altogether between {mb} and {mc}")


if __name__ == "__main__":
    run()