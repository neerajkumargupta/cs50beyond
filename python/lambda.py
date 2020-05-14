people = [
    {"name" : "Harry", "house": "Gryffindor"},
    {"name" : "Cho", "house": "Ravenclaw"},
    {"name" : "Draco", "house": "Slytherin"},
    {"name" : "Lavanya", "house": "Gupta"}
]

def sort(person):
    return person["house"]

#people.sort(key=sort)
people.sort(key=lambda person: person["name"])

print("sorted list")
print(people)