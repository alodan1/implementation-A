# implementation-A

## How it works
1. The client writes roommate data to roommates.json.
2. The server reads roommates.json, processes the data, and calculates how much each roommate owes.
3. The results are written to output.json.
4. The client reads output.json to retrieve the calculated debts.

## A. To request data from the microservice:
To request data, write a JSON object to roommates.json with a list of roommates, their utility contributions, and the amounts paid. Example request:
```
[
    {"name": "almog","utility": "water","amount": 120},
    {"name": "kabir","utility": "none","amount": 0},
    {"name": "Jemma", "utility": "electricy", "amount": 160},
    {"name": "Emily", "utility": "wifi", "amount": 35},
    {"name": "Fitz", "utility": "none", "amount": 0}
] 
```
Writing the Request in Python
```
import json

roommates = [
    {"name": "almog", "utility": "water", "amount": 120},
    {"name": "kabir", "utility": "none", "amount": 0},
    {"name": "Jemma", "utility": "electricity", "amount": 160},
    {"name": "Emily", "utility": "wifi", "amount": 35},
    {"name": "Fitz", "utility": "none", "amount": 0}
]

with open("roommates.json", "w") as file:
    json.dump(roommates, file, indent=4)
```
which reads the roommates json file and loads it into a variable called roommates

## B. To receive the data from the microservice:
Once the server processes the request, it writes the calculated debts to output.json.
example output:
```
[
    {
        "name": "kabir",
        "owes": "Jemma",
        "amount": 63.0
    },
    {
        "name": "Fitz",
        "owes": "Jemma",
        "amount": 34.0
    },
    {
        "name": "Fitz",
        "owes": "almog",
        "amount": 29.0
    },
    {
        "name": "Emily",
        "owes": "almog",
        "amount": 28.0
    }
]
```
Reading response in python:
```
import json

with open("output.json", "r") as file:
    transactions = json.load(file)
    print(transactions)  # Display calculated debts
```
1. The server starts by setting roommates.json to "ready".
2. It waits for the client to write roommate data.
3. Once the client writes the data, the server reads it and calculates how much each person owes.
4. It writes the results to output.json.
5. The client reads output.json to retrieve the calculations.
6. The process ends when the server detects "stop" in roommates.json.

## C. refer to UML.pdf
