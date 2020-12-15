import math
T = int(input())
R = []
for _ in range(T):
    x, y = map(int, input().split())
    dis = int(y - x)
    if dis <= 3:
        R.append(dis)
    else:
        n = int(math.sqrt(dis))
        if dis == n ** 2:
            R.append(2*n-1)
        elif n ** 2 < dis <= n ** 2 + n:
            R.append(2*n)
        else:
            R.append(2*n+1)

for i in R:
    print(i)
