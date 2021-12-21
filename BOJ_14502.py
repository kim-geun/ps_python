from collections import deque
from sys import stdin

# https://www.acmicpc.net/problem/14502

s = []
D = [(1, 0), (-1, 0), (0, 1), (0, -1)]
max_res = 0


def bfs():
    global max_res
    vis = [[False] * m for _ in range(n)]
    virus = deque()
    res = 0
    for i in range(n):
        for j in range(m):
            if s[i][j] == 2: virus.append((i, j))

    while virus:
        x, y = virus.popleft()
        for i, j in D:
            nx = x + i
            ny = y + j
            if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and s[nx][ny] == 0:
                vis[nx][ny] = True
                virus.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if s[i][j] == 0 and not vis[i][j]:
                res += 1

    max_res = max(max_res, res)


def dfs(cnt):
    if cnt == 3:
        bfs()
        return
    for i, j in wall:
        if s[i][j] == 0:
            s[i][j] = 1
            dfs(cnt + 1)
            s[i][j] = 0


n, m = map(int, input().split())
wall = []
for i in range(n):
    a = list(map(int, stdin.readline().split()))
    s.append(a);
    for j in range(m):
        if s[i][j] == 0: wall.append((i, j))
dfs(0)
print(max_res)