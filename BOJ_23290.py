from collections import deque
from sys import stdin
from copy import deepcopy

m, s = map(int, input().split())
fishes = []
ans = 0
max = 0
smell = [[0] * 4 for _ in range(4)]
graph = [[[] for i in range(4)] for j in range(4)]
pathes = []

fdx, fdy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
sdx, sdy = [-1, 0, 1, 0], [0, -1, 0, 1]

for i in range(m):
    x, y, d = map(int, stdin.readline().split())
    fishes.append([x - 1, y - 1, d - 1, False])

sx, sy = map(int, input().split())
shark = (sx - 1, sy - 1)


def init_graph():
    global graph
    for i in range(4):
        for j in range(4):
            graph[i][j].clear()


def kill_fish():
    global max, pathes, shark
    max = -1
    pathes = []
    find_route(0, shark[0], shark[1], [])
    shark = (pathes[2][0], pathes[2][1])
    for path in pathes:
        cx, cy = path[0], path[1]
        for fish in graph[cx][cy]:
            fishes[fish][3] = True
            smell[cx][cy] = 3


def delete_smell():
    global smell
    for i in range(4):
        for j in range(4):
            if smell[i][j] != 0: smell[i][j] -= 1


def find_route(level, x, y, routes):
    global max, pathes
    if level == 3:
        vis = [[False] * 4 for _ in range(4)]
        score = 0
        for route in routes:
            cx, cy = route[0], route[1]
            if vis[cx][cy]: continue
            vis[cx][cy] = True
            score += len(graph[cx][cy])
        if score > max:
            max = score
            pathes = deepcopy(routes)
        return

    for i in range(4):
        nx = x + sdx[i]
        ny = y + sdy[i]
        if 0 <= nx < 4 and 0 <= ny < 4:
            routes.append([nx, ny])
            find_route(level + 1, nx, ny, routes)
            routes.pop()


def move_fish():
    init_graph()
    delete_smell()
    global fishes, graph
    n_fishes = deepcopy(fishes)
    for idx, fish in enumerate(fishes):
        move = False
        cx = fish[0]
        cy = fish[1]
        dir = fish[2]
        for i in range(8):
            ndir = (dir - i + 8) % 8
            nx = cx + fdx[ndir]
            ny = cy + fdy[ndir]
            if nx < 0 or nx > 3 or ny < 0 or ny > 3: continue
            if nx == shark[0] and ny == shark[1]: continue
            if smell[nx][ny] == 0:
                fishes[idx] = [nx, ny, ndir, False]
                graph[nx][ny].append(idx)
                move = True
                break
        if not move: graph[cx][cy].append(idx)

    kill_fish()
    for fish in fishes:
        if not fish[3]:
            n_fishes.append(fish)

    fishes.clear()
    fishes += n_fishes

for i in range(s):
    move_fish()

print(len(fishes))