N,M=map(int,input().split())
alist=list(map(int,input().split()))
for i in range(M):
    a=input()
    if a[0]=="C":
        d=int(a[2])
        for j in range(N):
            alist[j]=(alist[j]+d) % 65535
    if a[0]=="Q":
        k=int(a[2])
        count=0
        for l in range(N):
            if bin(alist[l])[-k-1]=="1":
                count+=1
        print(count)