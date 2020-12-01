T = int(input())
tmp = ''
result = []

for i in range(T):
    R, S = list(map(str, input().split()))
    for j in range(len(S)):
        tmp += S[j]*int(R)
    result.append(tmp)
    tmp = ''

for k in result:
    print(k)
