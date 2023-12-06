from collections import defaultdict

result = 0
numbers = []
winning = []
multiplier = []

with open('input', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        numbers.append(set(x for x in line.split('|')[1].split(' ') if x))
        winning.append(set(x for x in line.split(':')[1].split('|')[0].split(' ') if x))
        multiplier.append(1)

for i, w in enumerate(winning):
    tmpres = 0
    for n in w:
        if n in numbers[i]:
            tmpres += 1
    for ii in range(i + 1, i + 1 + tmpres):
        if ii < len(multiplier):
            multiplier[ii] += multiplier[i]

print(multiplier)

print(sum(multiplier))