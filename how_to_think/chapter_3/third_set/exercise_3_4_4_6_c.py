people = ["Carrie", "Charlotte", "Sam", "Miranda"]

no_names_until_sam = 0
for name in people:
    no_names_until_sam += 1
    if name == "Sam":
        break

print("There are", no_names_until_sam, "names before Sam")
