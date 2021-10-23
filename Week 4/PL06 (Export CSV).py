import csv
def export(file_path, botimport):
    with open(file_path, "a") as file:
        for count in range(botimport):
            print("Exporting...")
            print("Enter the ID of the bot:")
            ID = str(input())
            print("\nName of the bot:")
            name = input()
            print("\nPaint of the bot:")
            paint = input()
            data = f"\n{ID}, {name}, {paint}\n"

            file.write(data)
            print("\nDone!")


def run():
    export("exported_bots.csv", 2)

if __name__ == "__main__":
    run()