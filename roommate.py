import json

class Person: #data structure to help organize each person
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

# opening and getting the info from the json file
with open("roommates.json", "r") as file:
    roommates = json.load(file)

# total bill
bill_total = sum(r["amount"] for r in roommates)
# the ammount of roommates
num_roommates = len(roommates)

# finds the average each roommate has to pay
average = bill_total / num_roommates if num_roommates > 0 else 0

# people list to store the roommates and their balances
people = []
for r in roommates:
    balance = r["amount"] - average
    people.append(Person(r["name"], balance))

# People who need to be paid back (sorted from highest to lowest balance).
payers = sorted([p for p in people if p.balance > 0], key=lambda x: x.balance, reverse=True)
# People who need to pay others (sorted from lowest to highest balance).
owers = sorted([p for p in people if p.balance < 0], key=lambda x: x.balance)

transactions = []

while payers and owers:
    # the first index are the people who are owed the most and owe the most
    payer = payers[0]
    ower = owers[0]

    amount_to_pay = min(payer.balance, -ower.balance)

    transactions.append({
        "name": ower.name,
        "owes": payer.name,
        "amount": amount_to_pay
    })

    payer.balance -= amount_to_pay
    ower.balance += amount_to_pay

    if payer.balance == 0:
        payers.pop(0)
    if ower.balance == 0:
        owers.pop(0)

with open("output.json", "w") as file:
    json.dump(transactions, file, indent=4)