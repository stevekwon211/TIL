T = int(input())
numList = []

for i in range(T):
    numList.append(list(map(int, input().split())))

for i in range(T):
    A = int(numList[i].pop())
    B = int(numList[i].pop())
    print("Case #%d: %d + %d = %d" % (i+1, B, A, A+B))
