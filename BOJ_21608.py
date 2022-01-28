# https://www.acmicpc.net/problem/21608
from heapq import heappush, heappop

N = int(input())
num = pow(N, 2)
students = []
dic = {}
grid = [[0] * N for _ in range(N)]
D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ans = 0

for _ in range(num):
    a = list(map(int, input().split()))
    students.append(a)
    dic[a[0]] = a[1:]

for student in students:
    pq = []
    for x in range(N):
        for y in range(N):
            like, empty = 0, 0
            if grid[x][y] == 0:
                for i, j in D:
                    nx = x + i
                    ny = y + j
                    if 0 <= nx < N and 0 <= ny < N:
                        if grid[nx][ny] != 0:
                            for idx in range(1, 5):
                                if grid[nx][ny] == student[idx]: like -= 1
                        else:
                            empty -= 1
                heappush(pq, [like, empty, x, y])
    _, _, x, y = heappop(pq)
    grid[x][y] = student[0]

for x in range(N):
    for y in range(N):
        cnt = 0
        for i, j in D:
            nx = x + i
            ny = y + j
            if 0 <= nx < N and 0 <= ny < N:
                if grid[nx][ny] in dic[grid[x][y]]: cnt += 1
        if cnt != 0: ans += pow(10, cnt - 1)

print(ans)