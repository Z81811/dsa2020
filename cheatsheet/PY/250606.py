import heapq
import sys
from collections import deque
startx,starty,endx,endy=map(int,input().split())
subwaylines=[]
for line in sys.stdin:
    line=line.strip()
    if not line:
        continue
    s=list(map(int,line.split()))
    i=0
    station=[]
    while i<len(s):
        x=s[i]
        y=s[i+1]
        i+=2
        if x==-1 and y==-1:
            break
        station.append((x,y))
    subwaylines.append(station)
graph={}
graph[(startx,starty)]={}
def dist(a,b):
    return ((a[0]-b[0])**2+abs(a[1]-b[1])**2)**0.5
for i in range(len(subwaylines)):
    for j in range(len(subwaylines[i])):
        if subwaylines[i][j] not in graph:
            graph[subwaylines[i][j]]={}
        if j<len(subwaylines[i])-1:
            graph[subwaylines[i][j]][subwaylines[i][j+1]]=graph[subwaylines[i][j+1]][subwaylines[i][j]]=dist(subwaylines[i][j],subwaylines[i][j+1])/40
        graph[subwaylines[i][j]][(endx,endy)]=dist(subwaylines[i][j],(endx,endy))/40
    for k in subwaylines[i]:
        graph[(startx,starty)][k]=dist((startx,starty),k)/10
heap=[(0,startx,starty)]
while heap:
    t,x,y=heapq.heappop(heap)
    if t>graph[(startx,starty)][(x,y)]:
        continue
    if x==endx and y==endy:
        print(t)
        break
    for nx,ny in graph[(x,y)]:
        newt=t+graph[(x,y)][(nx,ny)]
        if newt<graph[(startx,starty)][(nx,ny)]:
            heapq.heappush(heap,(newt,nx,ny))
            graph[(startx,starty)][(nx,ny)]=newt





