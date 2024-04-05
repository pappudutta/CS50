people = [
    {"name":"Harry", "house": "Gryffindor"},
    {"name":"Amit", "house": "Titabar"},
    {"name":"x-man", "house": "Jorhat"}
]

def f(person):
    return person["house"]

people.sort(key=f)

print(people)