num_list = []
num_slice = []

for i in range(0,3):
    num = int(input())
    num_list.append(num)

result = str(num_list[0]*num_list[1]*num_list[2])

for i in range(0,len(result)):
    num_slice.append(int(result[i]))

print(num_slice.count(0))
print(num_slice.count(1))
print(num_slice.count(2))
print(num_slice.count(3))
print(num_slice.count(4))
print(num_slice.count(5))
print(num_slice.count(6))
print(num_slice.count(7))
print(num_slice.count(8))
print(num_slice.count(9))

