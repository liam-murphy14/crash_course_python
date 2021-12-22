guests = ["abe linc", "jon hamm", "warren buffet", "elon"]
for guest in guests:
    message = f"welcome, {guest}"
    print(message)
print("abe cant make it")
guests[0] = "george washing machine"
for guest in guests:
    message = f"welcome, {guest}"
    print(message)
print("we got long table")
guests.append("johnny apples")
guests.insert(0, "billy gates")
guests.insert(2, "kevvy gates")
for guest in guests:
    message = f"welcome, {guest}"
    print(message)
    