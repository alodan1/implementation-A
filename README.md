# implementation-A

## A. To request data from the microservice:
send a JSON POST request to the endpoint. The request should contain a list of roommates, their utility contributions, and the amount they for the utility paid.

examples json file:
```
[
    {"name": "almog","utility": "water","amount": 120},
    {"name": "kabir","utility": "none","amount": 0},
    {"name": "Jemma", "utility": "electricy", "amount": 160},
    {"name": "Emily", "utility": "wifi", "amount": 35},
    {"name": "Fitz", "utility": "none", "amount": 0}
]
```
and the python file gets this information by
```
with open("roommates.json", "r") as file:
    roommates = json.load(file)
```
which reads the roommates json file and loads it into a variable called roommates

## B. To receive the data from the microservice:
once the request is processed, the microservice will return a JSON response containing the calculated debts, as in who owes who what.

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
it gets this information by first separating the ones who owe who and the ones who are owed. Then proceeds to calculate how much the owers owe the owed depending on the average everyone should be paying.


## C. refer to UML.pdf
