T = int(input())
result = 0
result_list = []
for i in range(0, T):
    A, B = map(int, input().split())
    result = A + B
    result_list.append(result)

result_list.reverse()

for j in range(0, T):
    print(result_list.pop())
