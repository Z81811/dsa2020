import math
import heapq


def main():
    # 读取家和学校的坐标
    home_x, home_y, school_x, school_y = map(int, input().split())

    # 存储所有地铁线路的输入行
    metro_lines = []
    while True:
        try:
            line = input().strip()
            if line:
                metro_lines.append(line)
        except EOFError:
            break

    # 管理所有节点的坐标和ID
    nodes = {}
    node_list = []

    # 添加家和学校到节点列表
    for coord in [(home_x, home_y), (school_x, school_y)]:
        if coord not in nodes:
            nodes[coord] = len(node_list)
            node_list.append(coord)
    home_id = nodes[(home_x, home_y)]
    school_id = nodes[(school_x, school_y)]

    # 第一次遍历地铁线路，收集所有站点
    for line in metro_lines:
        parts = list(map(int, line.split()))
        i = 0
        while i < len(parts):
            x = parts[i]
            y = parts[i + 1]
            i += 2
            if x == -1 and y == -1:
                break
            coord = (x, y)
            if coord not in nodes:
                nodes[coord] = len(node_list)
                node_list.append(coord)

    # 初始化邻接表（确保长度正确）
    n = len(node_list)
    adj = [[] for _ in range(n)]

    # 第二次遍历地铁线路，构建邻接表
    for line in metro_lines:
        parts = list(map(int, line.split()))
        stations = []
        i = 0
        while i < len(parts):
            x = parts[i]
            y = parts[i + 1]
            i += 2
            if x == -1 and y == -1:
                break
            coord = (x, y)
            stations.append(nodes[coord])

        # 添加相邻站点之间的边
        for j in range(len(stations) - 1):
            u = stations[j]
            v = stations[j + 1]
            x1, y1 = node_list[u]
            x2, y2 = node_list[v]
            distance = math.hypot(x2 - x1, y2 - y1)
            metro_time = (distance / 40000) * 60  # 转换为分钟
            adj[u].append((v, metro_time))
            adj[v].append((u, metro_time))

    # 预处理所有节点之间的步行时间
    walk_time = [[0.0] * n for _ in range(n)]
    for u in range(n):
        x1, y1 = node_list[u]
        for v in range(n):
            if u == v:
                walk_time[u][v] = 0.0
                continue
            x2, y2 = node_list[v]
            distance = math.hypot(x2 - x1, y2 - y1)
            walk_time[u][v] = (distance / 10000) * 60  # 步行时间

    # Dijkstra算法
    INF = float('inf')
    dist = [INF] * n
    dist[home_id] = 0.0
    heap = [(0.0, home_id)]
    heapq.heapify(heap)
    visited = [False] * n

    while heap:
        current_time, u = heapq.heappop(heap)
        if visited[u]:
            continue
        if u == school_id:
            break
        visited[u] = True

        # 处理地铁边
        for v, metro_time in adj[u]:
            if not visited[v] and current_time + metro_time < dist[v]:
                dist[v] = current_time + metro_time
                heapq.heappush(heap, (dist[v], v))

        # 处理步行边
        for v in range(n):
            if u == v or visited[v]:
                continue
            new_time = current_time + walk_time[u][v]
            if new_time < dist[v]:
                dist[v] = new_time
                heapq.heappush(heap, (dist[v], v))

    print(round(dist[school_id]))


if __name__ == "__main__":
    main()