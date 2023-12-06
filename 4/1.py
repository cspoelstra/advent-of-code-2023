

result = 0
with open('input', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        winning = {x for x in line.split(':')[1].split('|')[0].split(' ') if x}
        numbers = [x for x in line.split('|')[1].split(' ') if x]

        tmpres = 0
        for n in numbers:
            if n in winning:
                if tmpres == 0:
                    tmpres = 1
                else:
                    tmpres *= 2

        result += tmpres

print(result)