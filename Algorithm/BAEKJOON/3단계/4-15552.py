import sys

T = int(sys.stdin.readline())
numList = []

for i in range(T):
    numList.append(sys.stdin.readline().split())

for i in range(T):
    A = numList[i].pop()
    B = numList[i].pop()
    print(int(A) + int(B))
