line=input().strip()
parts=line.split(maxsplit=2)
kstr=""
R=int(parts[0])
C=int(parts[1])
bstr=parts[2]
alist=[[-1]*(C+2)]+[([-1]+[-2]*C+[-1]) for _ in range(R)]+[[-1]*(C+2)]
blist=[(0,1),(1,0),(0,-1),(-1,0)]
for i in bstr:
    if i.isalpha():
        kstr+=format(ord(i)-64,"05b")
    else:
        kstr+="00000"
w=len(kstr)
kstr+="0"*((R*C)-w)
b=0
p=q=1
for k in kstr:
    alist[p][q]=k
    if alist[p+blist[b][0]][q+blist[b][1]]==-2:
        p+=blist[b][0]
        q+=blist[b][1]
    else:
        b+=1
        b%=4
        p+=blist[b][0]
        q+=blist[b][1]
anslist=[]
for j in alist[1:-1]:
    for l in j[1:-1]:
        anslist.append(l)
print("".join(map(str,anslist)))







