live_cables = 0

print("How many live cables must I avoid?")
lc = int(input())

while live_cables < lc:
    print(f"Avoiding... ", end="")
    live_cables = live_cables + 1
    print(f"Done!{(live_cables)} live cables avoided.")


print("\nAll live cables have been avoided")

