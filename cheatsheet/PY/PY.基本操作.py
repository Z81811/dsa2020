# 基本输入输出
# 二、列表/数组操作
# 三、链表基本操作
# 四、栈和队列实现
# 五、二叉树遍历
# 递归遍历
#层序遍历
#二分查找
# 快速排序
#归并排序
#DFS,BFS




# 单行输入
n = int(input())  # 读取整数
s = input().strip()  # 读取字符串

# 多值输入
a, b = map(int, input().split())  # 读取两个整数
arr = list(map(int, input().split()))  # 读取整数列表

# 多行输入
n = int(input())
data = [input().strip() for _ in range(n)]

# 输出
print("Hello")  # 自动换行
print(a, b, sep=',')  # 自定义分隔符
print(f"{a} + {b} = {a+b}")  # f-string格式化









#列表数组操作
lst = [1, 2, 3]

# 增
lst.append(4)       # [1,2,3,4]
lst.insert(1, 5)    # [1,5,2,3,4]

# 删
lst.pop()           # 删除末尾，返回4
lst.pop(1)          # 删除索引1，返回5
lst.remove(2)       # 删除第一个2

# 查
x = lst[0]          # 获取第一个元素
idx = lst.index(3)  # 查找元素3的索引

# 改
lst[0] = 10         # [10,3]

# 其他
length = len(lst)   # 长度
lst.sort()          # 排序
lst.reverse()       # 反转









#链表操作
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 创建链表 1->2->3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# 遍历链表
p = head
while p:
    print(p.val)
    p = p.next

# 插入节点(在值为2的节点后插入4)
p = head
while p and p.val != 2:
    p = p.next
if p:
    new_node = ListNode(4)
    new_node.next = p.next
    p.next = new_node

# 删除节点(删除值为2的节点)
dummy = ListNode(0, head)
prev, curr = dummy, head
while curr:
    if curr.val == 2:
        prev.next = curr.next
        break
    prev, curr = curr, curr.next
head = dummy.next









#栈和队列
# 栈(列表实现)
stack = []
stack.append(1)  # push
stack.append(2)
top = stack[-1]  # peek
stack.pop()      # pop
is_empty = len(stack) == 0

# 队列(collections.deque)
from collections import deque
q = deque()
q.append(1)      # enqueue
q.append(2)
front = q[0]     # peek
q.popleft()      # dequeue
is_empty = len(q) == 0

# 栈(链表实现)
class StackNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, val):
        new_node = StackNode(val, self.top)
        self.top = new_node
    
    def pop(self):
        if not self.top: return None
        val = self.top.val
        self.top = self.top.next
        return val
    
    def peek(self):
        return self.top.val if self.top else None
    
    def is_empty(self):
        return self.top is None
    








#二叉树遍历
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 递归遍历
def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []

def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []

def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.val] if root else []

# 非递归遍历
def preorder_iter(root):
    stack, res = [], []
    while root or stack:
        while root:
            res.append(root.val)
            stack.append(root)
            root = root.left
        root = stack.pop()
        root = root.right
    return res

def inorder_iter(root):
    stack, res = [], []
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res

def postorder_iter(root):
    stack, res = [], []
    last_visited = None
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        peek = stack[-1]
        if peek.right and peek.right != last_visited:
            root = peek.right
        else:
            res.append(peek.val)
            last_visited = stack.pop()
    return res

# 层序遍历
def level_order(root):
    if not root: return []
    queue, res = [root], []
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.pop(0)
            level.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        res.append(level)
    return res









#二分查找
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1







#快速排序
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1




#归并排序
def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged









#DFS,BFS
# DFS递归
def dfs(node, visited):
    if not node: return
    visited.add(node)
    for neighbor in node.neighbors:
        if neighbor not in visited:
            dfs(neighbor, visited)

# DFS迭代
def dfs_iter(start):
    stack, visited = [start], set()
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in reversed(node.neighbors):  # 保持顺序
                if neighbor not in visited:
                    stack.append(neighbor)

# BFS
from collections import deque
def bfs(start):
    queue, visited = deque([start]), set()
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)