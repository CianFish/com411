import json
def read(file_path):
    print("Reading...")
    with open(file_path) as json.file:
        data = json.load(json.file)
        print("Done")

    return data

def save(file_path, data):
    print("Exporting...")
    with open(file_path, "w") as json.file:
        json.dump(data, json.file, indent = 4)
        print("Done!")

def run():
    data = read("robocity.json")
    save("exported.json", data)


if __name__ == "__main__":
    run()