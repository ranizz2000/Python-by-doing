f = open('csv.txt', 'r')
lines = f.readlines()
lines = [line.strip() for line in lines[1:]]
f.close()

for line in lines:
    person = line.split(',')
    #print(person)
    print(f'{person[0].title()} is {person[1]} years old and is studying {person[2].capitalize()} at {person[3]}')

