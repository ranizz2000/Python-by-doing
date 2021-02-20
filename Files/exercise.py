import json
with open('csv_file.txt', 'r') as f:
    contents = f.readlines()
    lines = [line.strip() for line in contents]
    for_json = []

    for line in lines:
        club,city,country = line.split(',')
        sport = {
            'club': club,
            'city': city,
            'country': country
        }
        for_json.append(sport)

with open('json_file.txt', 'w') as f2:
    json.dump(for_json, f2)

with open('json_file.txt', 'r') as f3:
    contents = json.load(f3)
    print(contents)
    print(type(contents))