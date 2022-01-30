# https://www.acmicpc.net/problem/17143
from sys import stdin

R, C, M = map(int, input().split())
grid = [[0] * C for _ in range(R)]
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
res = 0

for _ in range(M):
    r, c, s, d, z = map(int, stdin.readline().split())
    grid[r - 1][c - 1] = [s, d - 1, z]


def change_dir(dir):
    if dir == 0:
        return 1
    elif dir == 1:
        return 0
    elif dir == 2:
        return 3
    else:
        return 2


def move_shark():
    temp = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if grid[i][j] != 0:
                x, y, s, d, z = i, j, grid[i][j][0], grid[i][j][1], grid[i][j][2]
                while s > 0:
                    x += dx[d]
                    y += dy[d]
                    if 0 <= x < R and 0 <= y < C:
                        s -= 1
                    else:
                        x -= dx[d]
                        y -= dy[d]
                        d = change_dir(d)
                if temp[x][y] == 0:
                    temp[x][y] = [grid[i][j][0], d, z]
                else:
                    if temp[x][y][2] < z:
                        temp[x][y] = [grid[i][j][0], d, z]
    return temp

for i in range(C):
    for j in range(R):
        if grid[j][i] != 0:
            res += grid[j][i][2]
            grid[j][i] = 0
            break
    grid = move_shark()

print(res)