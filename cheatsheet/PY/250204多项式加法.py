n=int(input())
for i in range(n):
    alist=list(map(int,input().split()))
    blist=list(map(int,input().split()))
    c=alist+blist
    adict={}
    for j in range(0,len(c),2):
        if c[j+1]>=0:
            if c[j+1] in adict:
                adict[c[j+1]]+=c[j]
            else:
                adict[c[j+1]]=c[j]
    anslist=sorted(adict.items(),key=lambda x:x[0],reverse=True)
    ans=""
    for k in anslist:
        if k[1]!=0:
           astr="[ "+str(k[1])+" "+str(k[0])+" ] "
           ans+=astr
    print(ans.rstrip())
