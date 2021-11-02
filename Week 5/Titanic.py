import csv

records = []
headings = []

def load_data(file_path):
    print("Loading data...")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        headings = next(csv_reader)

        for line in csv_reader:
            records.append(line)

        print(f"Successfully loaded {len(records)} records")

def display_function():
    print("\n[1]" + " Display the names of all passengers")
    print("[2]" + " Display the number of passengers that survived")
    print("[3]" + " Display the number of passengers per gender")
    print("[4]" + " Display the number of passengers per age group")
    print("[5]" + " Display the number of survivors per age group")

    selection = int(input())
    return selection

def display_passenger_names(file_path):
    print("The names of the passengers are...\n")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        name = ""

        for values in csv_reader:
            name += f"{values[3]}\n"

    print(name)

def display_num_survivors():
    num_survived = 0

    for record in records:
        survival_status = int(record[1])
        if survival_status == 1:
            num_survived += 1

    print(f"{num_survived} passengers survived")

def display_passengers_per_gender():
    females = 0
    males = 0

    for record in records:
        gender = record[4]
        if gender == "male":
            males += 1
        elif gender == "female":
            females += 1

    print(f"Females: {females}, Males: {males}")

def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    no_age = 0

    for record in records:
        if record[5] != "":
            age = float(record[5])
            if age < 18:
                    children += 1
            elif age < 65 and age >= 18:
                    adults += 1
            elif age >= 65:
                    elderly += 1


    print(f"children: {children}, adults: {adults}, elderly: {elderly}")

def display_survivors_per_age_group():


def run():
    load_data("Titanic data.csv")
    selected_option = display_function()
    print(f"You have selected option: {selected_option}\n")

    if selected_option == 1:
        display_passenger_names("Titanic data.csv")
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option == 3:
        display_passengers_per_gender()
    elif selected_option == 4:
        display_passengers_per_age_group()



if __name__ == "__main__":
  run()