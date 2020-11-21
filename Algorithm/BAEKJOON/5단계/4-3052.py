num_list = []
num_rest = []

for i in range(0,10):
    num = int(input())
    num_list.append(num)

for i in range(0, 10):
    num_rest.append(num_list[i]%42)

num_rest = set(num_rest)
print(len(num_rest))
