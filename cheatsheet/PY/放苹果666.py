def pla(M,N):
    if N==1:
        return 1
    if M==N:
        return pla(M,N-1)+1
    if M>N:
        return pla(M,N-1)+pla(M-N,N)
    else:
        return pla(M,M)
M,N=map(int,input().split())
print(pla(M,N))