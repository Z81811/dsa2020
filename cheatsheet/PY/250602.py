from collections import deque
m=int(input())
n=int(input())
room=[]
for i in range(m):
    rlist=list(map(int,input().split()))
    room.append(rlist)
def canmove(roomlist,x,y,dx,dy):
    nx,ny=x+dx,y+dy
    if nx<0 or nx>=m or ny<0 or ny >=n:
        return False
    if dx==1 and dy==0:
        if room[x][y] in [0,1,2,4,3,5,6,7]:
            return True
        return False
    if dx==-1 and dy==0:
        if room[x][y] in [0,1,4,8,5,9,12,13]:
            return True
        else:
            return False
    if dx==0 and dy==1:
        if room[x][y] in [0,1,2,8,3,9,10,11]:
            return True
        else:
            return False
    if dx==0 and dy==-1:
        if room[x][y] in [0,2,4,8,6,10,12,14]:
            return True
        return False
roomsize=[]
visited=set()
for i in range(m):
    for j in range(n):
        if (i,j) not in visited:
            visited.add((i,j))
            size=0
            dire=[(-1,0),(0,1),(1,0),(0,-1)]
            queue=deque()
            queue.append((i,j))
            while queue:
                x,y=queue.popleft()
                size+=1
                for dx,dy in dire:
                    nx, ny = x + dx, y + dy
                    if canmove(room,x,y,dx,dy) and (nx,ny) not in visited:
                        queue.append((nx,ny))
                        visited.add((nx,ny))
            roomsize.append(size)
print(len(roomsize))
print(max(roomsize))

