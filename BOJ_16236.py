# https://www.acmicpc.net/problem/16236
from collections import deque
from sys import stdin

MAX_DIST = 987654321
n = int(input())
s = []
fishes = []
ans = 0
D = [(1, 0), (-1, 0), (0, -1), (0, 1)]

for i in range(n):
    a = list(map(int, stdin.readline().split()))
    s.append(a)
    for j in range(n):
        if a[j] == 9:
            shark = [i, j, 2, 0]
        else:
            if a[j] != 0:
                fishes.append([i, j, a[j], False, 0])

s[shark[0]][shark[1]] = 0

def bfs(sx, sy, fx, fy):
    q = deque()
    q.append([sx, sy, 0])
    vis = [[False] * n for _ in range(n)]
    while q:
        x, y, cnt = q.popleft()
        if x == fx and y == fy:
            return cnt
        for i, j in D:
            nx = x + i
            ny = y + j
            if 0 <= nx < n and 0 <= ny < n:
                if not vis[nx][ny] and s[nx][ny] <= shark[2]:
                    vis[nx][ny] = True
                    q.append([nx, ny, cnt + 1])
    return MAX_DIST


def move_shark():
    global shark, ans
    while True:
        flag = -1
        dist = MAX_DIST
        for idx, fish in enumerate(fishes):
            if fish[3] or fish[2] >= shark[2]: continue
            fish[4] = bfs(shark[0], shark[1], fish[0], fish[1])
            if fish[4] < dist:
                dist = fish[4]
                flag = idx
        if dist == MAX_DIST: break
        shark[3] += 1
        if shark[3] == shark[2]:
            shark[3] = 0
            shark[2] += 1
        shark[0], shark[1] = fishes[flag][0], fishes[flag][1]
        fishes[flag][3] = True
        ans += dist
    return ans

print(move_shark())