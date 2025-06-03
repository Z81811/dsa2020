while True:
    n,m=map(int,input().split())
    if m==0 and n==0:
        break
    else:
        alist=[i for i in range(1,n+1)]
        k=0
        while len(alist)>1:
            k+=1
            if k%m==0:
                alist=alist[1:]
            else:
                alist.append(alist.pop(0))
    print("".join(map(str,alist)))

