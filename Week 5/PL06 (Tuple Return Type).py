def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return (min(likelihoods), max(likelihoods))

def run():
    like = likelihood()
    print(f"Minimum likelihood of falling: {like[0]}%")
    print(f"Minimum likelihood of falling: {like[1]}%")

if __name__ == "__main__":
    run()
