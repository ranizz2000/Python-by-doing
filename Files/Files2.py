names = input("Enter your 3 friends. Seperated by commas.").split(',')

file = open("people.txt", "r")
people = file.readlines()
# for person in people:
#     print(person.rstrip('\n').casefold())
nearby = []
i = 0
for name in names:
    for person in people:
       i = i+1
       if name.casefold() == person.rstrip('\n').casefold():
           print(f"{i}. person = {person} and name = {name}")
           nearby.append(name)
print(nearby)