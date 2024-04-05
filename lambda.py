people = [
    {"name":"Harry", "house": "Gryffindor"},
    {"name":"Amit", "house": "Titabar"},
    {"name":"x-man", "house": "Jorhat"}
]

# def f(person):
#     return person["house"]

# Instead of defining above function I can use lambda

people.sort(key=lambda person: person["name"])

print(people)