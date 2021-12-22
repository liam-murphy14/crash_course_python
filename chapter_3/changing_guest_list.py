guests = ["abe linc", "jon hamm", "warren buffet", "elon"]
for guest in guests:
    message = f"welcome, {guest}"
    print(message)
print("abe cant make it")
guests[0] = "george washing machine"
for guest in guests:
    message = f"welcome, {guest}"
    print(message)