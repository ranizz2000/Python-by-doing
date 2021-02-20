import json

f = open("friends.txt", "r")
contents = json.load(f)
print(contents)

cars = [
    {'make': 'Suzuki', 'model': 'dia'},
    {'make': 'Nissin', 'model': 'ariya'}
]
f2 = open('dumping.txt', 'w')
json.dump(cars,f2)
f2.close()

f3 = open('dumping.txt', 'r')

print(json.load(f3))