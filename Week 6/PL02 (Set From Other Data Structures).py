def observed():
    observations = []
    for list in range(3):
        print("Please enter an observation")
        observations.append((input()))

    return observations

def run():
    print("Counting observations...")
    observations = observed()

    new = set()
    for words in observations:
        data = (words, observations.count(words))
        new.add(data)

    for data in new:
        print(f"{data[0]} observed {data[1]} times")

if __name__ == "__main__":
    run()


