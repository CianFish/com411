

set_a = set(("Apple", "Google", "Sony"))
set_a.add("X")
set_a.add("Y")

set_b = set(())
set_b.add("Y")

print(set_a.difference(set_b))