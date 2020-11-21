N, X = map(int, input().split())
num = map(int, input().split())
result = ""
for i in list(num):
    if i < X:
        result += ("%d " % i)
print(result)

