"""practicing imported modules and randomness"""
import random as r


class Die:
    """simulates a die"""


    def __init__(self, sides=6):
        self.sides = sides
    

    def roll(self):
        r.randint(1, self.sides)


def lottery():
    bank = list(range(0, 100))
    winner = []
    one = r.choice(bank)
    bank.remove(one)
    winner.append(one)
    two = r.choice(bank)
    bank.remove(two)
    winner.append(two)
    three = r.choice(bank)
    bank.remove(three)
    winner.append(three)
    four = r.choice(bank)
    bank.remove(four)
    winner.append(four)
    five = r.choice(bank)
    bank.remove(five)
    winner.append(five)
    six = r.choice(bank)
    bank.remove(six)
    winner.append(six)
    print(winner)
    return winner


my_ticket = [23, 56, 32, 76, 78, 50]
counter = 0
match = False
while not match:
    counter += 1
    match = True
    winner = lottery()
    for i in range(0, 6):
        if my_ticket[i] != winner[i]:
            match = False
            break
print(f"you won in {counter} tries")