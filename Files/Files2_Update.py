names = input("Enter your friends' names. (separate with commas and no spaces)").split(",")

file = open("people.txt", "r")
people = file.readlines()
people = [line.strip() for line in people]
file.close()

names_set = set(name.casefold() for name in names)
people_set = set(person.casefold() for person in people)

nearby = names_set.intersection(people_set)
# print(nearby)

file2 = open("nearby.txt", "w")
for i in nearby:
    file2.write(f"{i}\n")
file2.close()