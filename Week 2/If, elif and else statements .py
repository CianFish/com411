print("Is it sunny?")
is_sunny = input().lower()

print("Is it windy?")
is_windy = input().lower()

if is_sunny == "yes" and is_windy == "yes":
        print("Clothes are dry")
elif is_sunny == "yes" and is_windy == "no":
    print("clothes are slowly drying")
elif is_sunny == "no" and is_windy == "yes":
    print("clothes are slowly drying")
else:
    print("Clothes are not dry")

