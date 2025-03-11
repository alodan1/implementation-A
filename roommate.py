import json
import time

class Person:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

# Initialize roommates.json with "ready"
with open("roommates.json", "w") as file:
    json.dump("ready", file, indent=4)

while True:
    time.sleep(5)  # Wait before reading

    # Read roommates.json
    with open("roommates.json", "r") as file:
        roommates = json.load(file)

    if roommates == "ready":
        continue  # Wait for the client to write roommates data
    
    if roommates == "stop":
        print("Server shutting down.")
        break  # Exit the while loop

    if isinstance(roommates, list):  # Roommate data received
        with open("roommates.json", "w") as file:
            json.dump("reading data", file, indent=4)  # Indicate processing

        # Calculate total bill
        bill_total = sum(r["amount"] for r in roommates)
        num_roommates = len(roommates)

        # Calculate average amount each roommate has to pay
        average = bill_total / num_roommates if num_roommates > 0 else 0

        # Create list of Person objects
        people = [Person(r["name"], r["amount"] - average) for r in roommates]

        # Sort people into payers (positive balance) and owers (negative balance)
        payers = sorted([p for p in people if p.balance > 0], key=lambda x: x.balance, reverse=True)
        owers = sorted([p for p in people if p.balance < 0], key=lambda x: x.balance)

        transactions = []

        while payers and owers:
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

        # Write transactions to output.json
        with open("output.json", "w") as file:
            json.dump(transactions, file, indent=4)
            

        # Keep server running instead of exiting
