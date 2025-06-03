import heapq
P=int(input())
graph={}
for i in range(P):
    place=input()
    graph[place]={}
Q=int(input())
for i in range(Q):
    a,b,l=map(str,input().split())
    l=int(l)
    graph[a][b]=l
    graph[b][a]=l

def dijkstra(start,end):
    distance={node:float('inf') for node in graph}
    parent={node:None for node in graph}
    heap=[]
    distance[start]=0
    heapq.heappush(heap,(0,start))
    while heap:
        dist,node=heapq.heappop(heap)
        if node==end:
            break
        if distance[node]<dist:
            continue
        for k,v in graph[node].items():
            new_dist=dist+v
            if new_dist<distance[k]:
                distance[k]=new_dist
                parent[k]=node
                heapq.heappush(heap,(new_dist,k))
    if parent[end] is None and start!=end:
        return None
    path=[]
    node=end
    while node is not None:
        path.append(node)
        temp=parent[node]
        if temp:
            path.append(f"({graph[temp][node]})")
        node=temp
    return path[::-1]
R=int(input())
for i in range(R):
    a,b=map(str,input().split())
    if dijkstra(a,b):
        print("->".join(map(str,dijkstra(a,b))))
