import re

hand = open('Actual data')
result = []
numlist = list()
for line in hand:
    temp = (re.findall('[0-9]+', line))
    result.append(sum(list(map(int, temp))))

print(sum(result))