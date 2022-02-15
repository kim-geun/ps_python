# https://www.acmicpc.net/problem/15686
from sys import stdin
from collections import deque
from itertools import combinations

INF = 1e9
N, M = map(int, input().split())
s = []
chickens = deque()
homes = deque()

for i in range(N):
    a = list(map(int, stdin.readline().split()))
    for j in range(N):
        if a[j] == 2:
            chickens.append([i, j])
        elif a[j] == 1:
            homes.append([i, j])
        s.append(a)


def dist(hx, hy, cx, cy):
    return abs(hx - cx) + abs(hy - cy)


def pick_chicken():
    items = list(combinations(chickens, M))
    ans = INF
    for item in items:
        res = 0
        for home in homes:
            hx, hy = home
            tmp = INF
            for pos in item:
                cx, cy = pos
                if dist(hx, hy, cx, cy) < tmp:
                    tmp = dist(hx, hy, cx, cy)
            res += tmp
        if res < ans:
            ans = res
    return ans


print(pick_chicken())