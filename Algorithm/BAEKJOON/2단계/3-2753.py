A = int(input())
print(['','01'[A%400==0 or (A%4==0 and A%100!=0)]][1<=A<=4000])
