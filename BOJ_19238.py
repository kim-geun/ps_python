# https://www.acmicpc.net/problem/19238
from sys import stdin
from collections import deque
from heapq import heappop, heappush

D = [(-1, 0), (1, 0), (0, 1), (0, -1)]

n, m, fuel = map(int, input().split())
INF = int(1e9)
s = [list(map(int, stdin.readline().split())) for _ in range(n)]
taxi_pos = list(map(int, input().split()))
guests = []
picked = [False for _ in range(m)]

for _ in range(m):
    a = list(map(int, input().split()))
    guests.append(a)


def bfs():
    global taxi_pos
    q = deque()
    tx, ty = taxi_pos[0] - 1, taxi_pos[1] - 1
    chk = [[False] * n for _ in range(n)]
    table = [[INF] * n for _ in range(n)]
    table[tx][ty] = 0
    q.append([tx, ty])
    chk[tx][ty] = True

    while q:
        x, y = q.popleft()
        for i, j in D:
            nx = x + i
            ny = y + j
            if 0 <= nx < n and 0 <= ny < n:
                if not chk[nx][ny]:
                    if s[nx][ny] != 1:
                        chk[nx][ny] = True
                        table[nx][ny] = table[x][y] + 1
                        q.append([nx, ny])

    return table


def find_guest():
    global s, fuel, picked
    table = bfs()
    pq = []

    for i in range(m):
        if not picked[i]:
            x, y = guests[i][0] - 1, guests[i][1] - 1
            dist = table[x][y]
            if fuel - dist >= 0:
                heappush(pq, [dist, x, y, i])

    if not pq: return -1
    dist, _, _, guest_index = heappop(pq)
    fuel -= dist
    picked[guest_index] = True

    return guest_index


def go_dst(guest_index):
    global fuel
    table = bfs()
    x, y = guests[guest_index][2] - 1, guests[guest_index][3] - 1
    dist = table[x][y]
    if fuel - dist < 0: return -1
    return dist


ok = True
cnt = m
while cnt:
    guests_idx = find_guest()
    if guests_idx == -1:
        ok = False
        break
    taxi_pos = guests[guests_idx][0], guests[guests_idx][1]
    dist = go_dst(guests_idx)
    if dist == -1:
        ok = False
        break
    fuel += dist
    taxi_pos = guests[guests_idx][2], guests[guests_idx][3]
    cnt -= 1

if ok:
    print(fuel)
else:
    print(-1)