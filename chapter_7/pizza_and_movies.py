topping = ""
toppings = []
print("type 'quit' to quit")
while topping != "quit":
    topping = (input("what would you like on your pizza ?? ")).lower().strip()
    if topping == "quit":
        continue
    toppings.append(topping)
print(f"your pizza has {toppings} on it")

price = 0
print("type quit to quit")
while price >= 0:
    age = input("what is your age ?? ")
    if age.lower().strip() == "quit":
        price = -1
        continue
    age = int(age)
    if age < 3:
        price = 0
    elif age < 13:
        price = 10
    else:
        price = 15
    print(f"your ticket is {price} dollars")