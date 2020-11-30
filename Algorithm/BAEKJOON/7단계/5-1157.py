word = input().upper()
alpha = []

for i in set(word):
    alpha.append(word.count(i))

maxloc = [i for i, j in enumerate(alpha) if j == max(alpha)]

if len(maxloc) > 1:
    print("?")
else :
    print(list(set(word))[alpha.index(max(alpha))])
