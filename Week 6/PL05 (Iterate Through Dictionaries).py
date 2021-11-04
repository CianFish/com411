def pattern(sequences):
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}

    return sequences


def display_keys(sequences):
    print("\nKeys:")
    for key in sequences:
        print(key)

def display_values(sequences):
    print("\nValues:")
    for values in sequences.values():
        print(values)

def display_items(sequences):
    print("\nPairs")
    for key, values in sequences.items():
        print(f"{key}: {values}")

def run():
    sequences = {"Short Sequence":3, "Medium Sequence":2, "Long Sequence":1}
    pattern(sequences)
    display_keys(sequences)
    display_values(sequences)
    display_items(sequences)


if __name__ == "__main__":
    run()
