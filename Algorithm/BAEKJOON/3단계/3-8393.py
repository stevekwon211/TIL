n = int(input())
i = 0
exec('i = i + 1;''n += i;' * (n-1))
print(n)
