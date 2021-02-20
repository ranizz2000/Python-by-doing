import csv as c
movies = [
    {'name': 'The matrix', 'director': 'Batuchi'},
    {'name': 'Mone Shwe Yee', 'director': 'Shwe Yee'},
    {'name': 'Eain Met', 'director': 'Win Pa'}
]
def intoit(output):
    with open('csv2.txt', 'w') as f:
      c.writer()
    f.close()

intoit(movies)

def outit():
    with open('csv2.txt', 'r') as f:
        lines = f.readlines()
        for i in lines[1:]:
            print(i.strip().split(','))
    f.close()

outit()