import json
import time

while True:
    # Read roommates.json
    with open("roommates.json", "r") as file:
        data = json.load(file)

    # If file contains "ready", write roommates data
    if data == "ready":
        roommates = [
            {"name": "almog", "utility": "water", "amount": 120},
            {"name": "kabir", "utility": "none", "amount": 0},
            {"name": "Jemma", "utility": "electricity", "amount": 160},
            {"name": "Emily", "utility": "wifi", "amount": 35},
            {"name": "Fitz", "utility": "none", "amount": 0}
        ]
        with open("roommates.json", "w") as file:
            json.dump(roommates, file, indent=4)

    time.sleep(10)  # Wait before checking again

    # Read roommates.json again to check for processing status
    with open("roommates.json", "r") as file:
        data = json.load(file)

    if data == "reading data":
        with open("output.json", "r") as file2:
            transactions = json.load(file2)
            print(transactions)  # Display transactions

        with open("roommates.json", "w") as file:
            json.dump("stop", file, indent=4)
        break  # Instead of exit(1), use break to end the loop properly