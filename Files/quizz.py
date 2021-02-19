file = open('question.txt', 'r')
questions = file.readlines()
file.close()

score = 0
i = 0

for question in questions:
    p = question.split('=')
    i = i + 1
    if p[1].strip() == input(f'{p[0]} = '):
        score = score + 1

final_score = score/ i

f = open('result.txt', 'w')
f.write(f'Your final score is {score}/{i}.')
f.close()
