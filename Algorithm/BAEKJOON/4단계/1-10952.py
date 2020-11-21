results = []
A=1
B=1

while(A != 0 and B != 0):
    A, B = map(int, input().split())
    results.append(A + B)

results.remove(0)

for result in results:
    print(result)

