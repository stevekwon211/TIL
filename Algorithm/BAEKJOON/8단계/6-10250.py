R = []
for i in range(int(input())):
    H, W, N = map(int,input().split())
    Y = N%H
    X = N//H+1
    
    if Y==0:
        Y=H
        X -= 1
    R.append(Y*100+X)
        
for i in R: print(i)
