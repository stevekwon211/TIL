c_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for i in c_alpha:
    word = word.replace(i, 'w')

print(len(word))
