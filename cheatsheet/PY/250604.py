import heapq

S = int(input())
for i in range(S):
    N, M = map(int, input().split())
    maze = []
    for j in range(N):
        s = input().strip()
        maze.append(s)
        if "r" in s:
            startx, starty = j, s.index("r")
        if "a" in s:
            endx, endy = j, s.index("a")
    time = [[float("inf")]*M for _ in range(N)]
    time[startx][starty] = 0
    heap = [(0, startx, starty)]
    flag = False
    dire = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while heap:
        t, x, y = heapq.heappop(heap)
        if t > time[x][y]:
            continue
        if x == endx and y == endy:
            print(t)
            flag = True
            break
        for dx, dy in dire:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] != "#":
                weight = float("inf")
                if maze[nx][ny] in ["@","a"]:
                    weight = 1
                if maze[nx][ny] == "x":
                    weight = 2
                newt = t + weight
                if newt < time[nx][ny]:
                    time[nx][ny] = newt
                    heapq.heappush(heap, (time[nx][ny], nx, ny))
    if not flag:
        print("Impossible")
