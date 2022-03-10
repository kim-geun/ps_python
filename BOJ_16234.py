# https://www.acmicpc.net/problem/16234
from sys import stdin
from collections import deque

N, L, R = map(int, input().split())
A = [list(map(int, stdin.readline().split())) for _ in range(N)]
D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 0

while True:
    Move = False
    vis = [[False] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not vis[r][c]:
                vis[r][c] = True
                q = deque()
                blocks = deque()
                q.append([r, c])
                blocks.append([r, c])
                total = A[r][c]
                while q:
                    cx, cy = q.popleft()
                    for dx, dy in D:
                        nx = cx + dx
                        ny = cy + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            dif = abs(A[nx][ny] - A[cx][cy])
                            if L <= dif <= R and not vis[nx][ny]:
                                vis[nx][ny] = True
                                total += A[nx][ny]
                                q.append([nx, ny])
                                blocks.append([nx, ny])
                if len(blocks) != 1:
                    Move = True
                    npop = total // len(blocks)
                    for block in blocks:
                        cx, cy = block
                        A[cx][cy] = npop
    if Move:
        cnt += 1
    else:
        print(cnt)
        break
