import re

# PART 1
with open('input.txt', 'r') as f:
    data = f.read()
search = re.findall(r'mul\([0-9]+,[0-9]+\)', data)

res = 0
for match in search:
    n1, n2 = re.findall(r'[0-9]+[,][0-9]+', match)[0].split(',')
    res += int(n1) * int(n2)
print(res)

# PART 2
search = re.findall(r"mul\([0-9]+,[0-9]+\)|don?'?t?\(\)", data)

res = 0
flag = True
for match in search:
    if match == 'do()':
        flag = True
    elif match == "don't()":
        flag = False
    else:
        n1, n2 = re.findall(r'[0-9]+[,][0-9]+', match)[0].split(',')
        val = int(n1) * int(n2)
        res += val * flag
print(res)