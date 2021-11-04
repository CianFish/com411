def observed():
    observations = []

    for count in range(5):
        print("Please enter an observation:")
        observations.append(input())

    return observations

def remove_observations(observations):
    print("Do you wish to remove an observation?")
    ans = input()
    if ans == "yes":
        print("How many observations would you like to remove?")
        list = int(input())
        for word in range(list):
            print("What observation would you like to remove?")
            observations.remove(input())
            print("Done!")

def run():
    print("Counting observations...")
    observations = observed()
    remove_observations(observations)

    new = set()
    for words in observations:
        data = (words, observations.count(words))
        new.add(data)



    for data in new:
        print(f"{data[0]} observed {data[1]} times")

if __name__ == "__main__":
    run()