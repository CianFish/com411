def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run():
    print("Moving...")
    path = movements()
    print(f"Move forward {path[0]} for {path[1]} steps")
    print(f"Move forward {path[2]} for {path[3]} steps")
    print(f"Move forward {path[4]} for {path[5]} steps")
    print(f"Move forward {path[6]} for {path[7]} steps")

if __name__ == "__main__":
    run()