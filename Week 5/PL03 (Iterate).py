def directions():
    direction = [ "Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return direction

def menu():
    print("Please select a direction:")
    direction = directions()
    for list in range(len(directions())):
        call = direction[list]
        print(f"{list}: {call} ")

def run():
    menu()

if __name__ == "__main__":
    run()