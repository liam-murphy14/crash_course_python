brand = input("what kinda car you want ?? ")
print(f"ill try to find a {brand}")

guests = input("how many people you got ?? ")
guests = int(guests)
if guests > 8:
    print("You gotta wait for a table homes")

num = input("gimme a number ")
num = int(num)
if num % 10 == 0:
    print("multiple of ten")
else:
    print("not a multiple of ten")