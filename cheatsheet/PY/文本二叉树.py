class node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
def preorder(root):
    ans=[]
    def helper(root):
        if root==None:
            return
        ans.append(root.value)
        helper(root.left)
        helper(root.right)
    helper(root)
    return "".join(ans)
def inorder(root):
    ans=[]
    def helper(root):
        if root==None:
            return
        helper(root.left)
        ans.append(root.value)
        helper(root.right)
    helper(root)
    return "".join(ans)
def postorder(root):
    ans=[]
    def helper(root):
        if root==None:
            return
        helper(root.left)
        helper(root.right)
        ans.append(root.value)
    helper(root)
    return "".join(ans)
n=int(input())
for k in range(n):
    nodes=[]
    while True:
        line = input().strip()
        if line == "0":
            break
        level=line.count("-")
        nodes.append((level,line[-1]))
    tree={}
    if not nodes:
        print()
    if len(nodes)==1:
        print(nodes[0][1])
        print(nodes[0][1])
        print(nodes[0][1])
        if k!=n-1:
            print()
        continue
    for i in range(len(nodes)-1):
        if nodes[i][1]=="*":
            continue
        if nodes[i][1] not in tree:
            tree[nodes[i][1]]=node(nodes[i][1])
        if  nodes[i+1][1]!="*" and nodes[i+1][0]==nodes[i][0]+1:
            if nodes[i + 1][1] not in tree:
                tree[nodes[i+1][1]]=node(nodes[i+1][1])
            tree[nodes[i][1]].left=tree[nodes[i+1][1]]
        for j in range(i+2,len(nodes)):
            if nodes[j][0]==nodes[i][0]+1 and nodes[j][1]!="*":
                if nodes[j][1] not in tree:
                    tree[nodes[j][1]]=node(nodes[j][1])
                if tree[nodes[j][1]].parent:
                   tree[nodes[j][1]].parent.right=None
                tree[nodes[i][1]].right=tree[nodes[j][1]]
                tree[nodes[j][1]].parent = tree[nodes[i][1]]
                break
    print(preorder(tree[nodes[0][1]]))
    print(postorder(tree[nodes[0][1]]))
    print(inorder(tree[nodes[0][1]]))
    if k!=n-1:
       print()





