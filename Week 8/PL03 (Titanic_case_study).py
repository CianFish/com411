import matplotlib.pyplot as plt
import csv


def read_data():
    with open("titanic.csv") as file:
        csv_reader = csv.reader(file)
        tit_data = {'PassengerID': [], 'Survived': [], "Pclass": [], "Name": [], "Sex": [], "Age": [], "SibSp": [], "Parch": [], "Ticket": [], "Fare": [], "Cabin": [], "Embarked": []}
        heading = next(csv_reader)
        for line in csv_reader:
            tit_data["PassengerID"].append(line[0])
            tit_data["Survived"].append(line[1])
            tit_data["Pclass"].append(line[2])
            tit_data["Name"].append(line[3])
            tit_data["Sex"].append(line[4])
            tit_data["Age"].append(line[5])
            tit_data["SibSp"].append(line[6])
            tit_data["Parch"].append(line[7])
            tit_data["Ticket"].append(line[8])
            tit_data["Fare"].append(line[9])
            tit_data["Cabin"].append(line[10])
            tit_data["Embarked"].append(line[11])

    return tit_data

def run():
    data = read_data()

    fig, axes = plt.subplots(2,2)

    x0 =
    axes[0,0]

run()

