import json
def read(file_path):
    with open(file_path) as json.file:
        data = json.load(json.file)
        city_name = data["city"]
        print(f"City Name: {city_name}")

        pop_size = data["population"]
        print(f"Population Size {pop_size}")

        for bot in data["bots"]:
            bot_name = bot["name"]
            stat = bot["stats"]
            print(f"{bot_name} has the following stats: {stat}")

def run():
    read("robocity.json")

if __name__ == "__main__":
    run()
