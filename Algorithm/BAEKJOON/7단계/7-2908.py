num = list(map(str, input().split()))
num1 = ''.join(list(reversed(num[0])))
num2 = ''.join(list(reversed(num[1])))
if num1 < num2:
    print(num2)
else:
    print(num1)
