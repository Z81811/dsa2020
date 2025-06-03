#kruskal算法，最小生成树，边按权重排序，不生成环的加进来
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        rootx=self.find(x)
        rooty=self.find(y)
        if rootx != rooty:
            self.parent[rootx]=rooty
def kruskal(n,edges):
    sortedge=sorted(edges,key=lambda x:x[2])
    uf=UnionFind(n)
    mst=[]
    weight=0
    for u,v,w in sortedge:
        if uf.find(v)!=uf.find(u):
            uf.union(u,v)
            mst.append((u,v,w))
            weight+=w
            if len(mst)==n-1:
                break
    return weight

n=int(input())
edges=[]
for i in range(n-1):
    alist=list(map(str,input().split()))
    if len(alist)>2:
        for j in range(2,len(alist)-1,2):
            edges.append((i,ord(alist[j])-ord("A"),int(alist[j+1])))
print(kruskal(n,edges))