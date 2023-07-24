#Initialise empty dictionary
d = {}
d2 = dict()
#initialise non-empty dictionary
phonebook = {"Thomas":7743434310, "Ruud": 734343434312, "juLY": 776591029}
#Print individual elements
name = input("Who you gonna call ")
if name in phonebook:
    print(f"Calling...{phonebook[name]}")
else:
    print(f"No number for {name}")
#Zipping two lists together into a dictionary
names = ["Marius", "Nazaret", "Michaela"]
ages = [23, 22, 21]
people = dict(zip(names, ages))
print(people)
#Values two
#Traveling Dictionaries - accessing keys/values
for thing in people:
    print(thing)
for thing in people.values():
    print(thing)
for v, k in people.items():
    print(f"Person {k} is {v} years old")
