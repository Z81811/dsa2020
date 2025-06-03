from collections import deque
T=int(input())
for t in range(T):
    R,C=map(int,input().split())
    maze=[]
    for i in range(R):
        s=input()
        maze.append(s)
        if "S" in s:
            startx,starty=i,s.index("S")
        if "E" in s:
            endx,endy=i,s.index("E")
    queue=deque()
    queue.append((startx,starty,0))
    visited=set()
    visited.add((startx,starty))
    directions=[(0,1),(1,0),(-1,0),(0,-1)]
    flag=False
    while queue:
        x,y,time=queue.popleft()
        if x==endx and y==endy:
            print(time)
            flag=True
            break
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<R and 0<=ny<C and maze[nx][ny]!="#" and (nx,ny) not in visited:
                queue.append((nx,ny,time+1))
                visited.add((nx,ny))
    if not flag:
        print("oop!")





