import csv
import process
import tui


def read_data(file_path):
    print(f"Reading data from {file_path}")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)
        data = []

        for line in csv_reader:
            data.append(line)

    return data

def run():
    athlete_data = read_data("athlete_events.csv")

    while True:
        selection = tui.menu()
        if selection == "years":
            process.list_years(athlete_data)
        elif selection == "tally":
            pass
        elif selection == "team":
            pass
        elif selection == "exit":
            break
        else:
            tui.error("Invalid Selection!")


if __name__ == "__main__":
    run()