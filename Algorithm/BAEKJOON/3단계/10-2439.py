T = int(input())
S = "*"

for i in range(T):
    T -= 1
    print("%s%s" % (T*" ",S))
    S += "*"
