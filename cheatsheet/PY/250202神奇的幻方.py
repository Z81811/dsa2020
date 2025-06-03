N=int(input())
alist=[[0]*(2*N-1) for _ in range(2*N-1)]
alist[0][N-1]=1
x=0
y=N-1
for i in range(2,(2*N-1)**2+1):
    if x-1>=0 and y+1<=2*N-2 and alist[x-1][y+1]==0:
        x-=1
        y+=1
    elif x==0 and y!=2*N-2:
        x=2*N-2
        y+=1
    elif y==2*N-2 and x!=0:
        x-=1
        y=0
    else:
        x+=1
    alist[x][y]=i
for k in alist:
    print(" ".join(map(str,k)))

