T=int(input())
for j in range(T):
    n=int(input())
    alist=list(map(int,input().split()))
    a=[]
    flag=True
    for i in alist:
        if i>0:
            a.append(abs(i))
        else:
            if a==[]:
                flag=False
                break
            elif abs(i)!=a[0]:
                flag=False
                break
            else:
                a.pop(0)
    if flag:
           print(f"Case {j+1}: yes")
    else:
        print(f"Case {j+1}: no")