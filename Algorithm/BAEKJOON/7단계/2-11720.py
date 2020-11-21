N = int(input())
num = list(map(str, input().split()))
result = 0
for i in range(0,N):
    result += int(num[0][i])
print(result)
