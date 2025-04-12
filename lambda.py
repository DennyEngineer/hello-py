people = [
    {"name":"Denzel", "house": "Accra"},
    {"name":"Enoch", "house": "Ablekuma"},
    {"name":"Myles", "house": "Kasoa"}
]

people.sort(key=lambda person: person["name"])

print(people)