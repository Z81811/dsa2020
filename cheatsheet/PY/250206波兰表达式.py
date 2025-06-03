alist=list(map(str,input().split()))
num=[]
cal=[]
def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
for i in alist[::-1]:
    if is_float(i):
        num.append(float(i))
    elif i=="+":
        l=num.pop()+num.pop()
        num.append(l)
    elif i=="*":
        l=num.pop()*num.pop()
        num.append(l)
    elif i=="/":
        l=num.pop()/num.pop()
        num.append(l)
    elif i=="-":
        l=num.pop()-num.pop()
        num.append(l)
print(f"{num[0]:.1f}")