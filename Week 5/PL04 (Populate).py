def directions():
    direction = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return direction

def menu():
    print("\nPlease select a direction:")
    call = directions()
    for list in range(len(call)):
        print(f"{list}: {call[list]}")
    index = int(input())
    return call[index]

def run():
    route = []
    print("Working out escape route...")
    for lis in range(5):
        route.append(menu())
    print(f"Escape route: {route}")


if __name__ == "__main__":
    run()