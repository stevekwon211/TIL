import sys
results = []
A=1
B=1
try:
    while(A != 0 and B != 0):
        A, B = list(map(int, sys.stdin.readline().split()))
        results.append(A + B)

except ValueError as ve:
   for result in results:
        print(result)

