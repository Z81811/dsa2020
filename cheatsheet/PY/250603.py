while True:
    n,k=map(int,input().split())
    if n==k==-1:
        break
    board=[]
    for i in range(n):
        row=input().strip()
        f=[j for j,i,in enumerate(row) if i=="#"]
        board.append(f)
    count=0
    def backtrack(i,mask,c):
        global count
        if c==k:
            count+=1
            return
        if i>=n:
            return
        if n-i<k-c:
            return
        backtrack(i+1,mask,c)
        for j in board[i]:
            if not (mask & (1<<j)):
                backtrack(i+1,mask|(1<<j),c+1)
    backtrack(0,0,0)
    print(count)


