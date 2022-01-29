# https://www.acmicpc.net/problem/16235
from collections import deque
from sys import stdin
from heapq import heappop, heappush

N, M, K = map(int, input().split())
A = [list(map(int, stdin.readline().split())) for _ in range(N)]
grid = [[deque() for _ in range(N)] for _ in range(N)]
land = [[5] * N for _ in range(N)]
D = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
ans = 0
for _ in range(M):
    x, y, z = map(int, input().split())
    grid[x - 1][y - 1].append(z)

while K:
    K -= 1
    for x in range(N):
        for y in range(N):
            len_t = len(grid[x][y])
            for i in range(len_t):
                if grid[x][y][i] <= land[x][y]:
                    land[x][y] -= grid[x][y][i]
                    grid[x][y][i] += 1
                else:
                    for _ in range(i, len_t):
                        land[x][y] += grid[x][y].pop() // 2
                    break

    for x in range(N):
        for y in range(N):
            for i in grid[x][y]:
                if i % 5 == 0:
                    for dx, dy in D:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            grid[nx][ny].appendleft(1)
            land[x][y] += A[x][y]

for x in range(N):
    for y in range(N):
        ans += len(grid[x][y])

print(ans)