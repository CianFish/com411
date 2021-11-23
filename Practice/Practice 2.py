import csv


def min_max(file_path):
    with open("athlete.csv") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        min = 2022
        for row in csv_reader:
            if int(row[9]) < min:
                min = int(row[9])

    print(min)


def run():
    min_max("athlete.csv")



if __name__ == "__main__":
    run()