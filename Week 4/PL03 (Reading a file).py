def search(file_path):
    print("Searching...")
    with open(file_path) as file:
        for line in file:
            print(f"Looked in {line.strip()}")


def run():
    search("library.txt")

if __name__ == "__main__":
    run()