sandwich_orders = ["pastrami", "hoagie", "blt", "pastrami", "caprisi"]
finished = []
while sandwich_orders:
    current = sandwich_orders.pop()
    print(f"making {current}")
    finished.append(current)
print(finished)

sandwich_orders = ["pastrami", "hoagie", "blt", "pastrami", "caprisi"]
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")
print(sandwich_orders)