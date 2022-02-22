# https://www.acmicpc.net/problem/17779
from sys import stdin
from collections import deque

N = int(input())
A = [list(map(int, stdin.readline().split())) for _ in range(N)]

D = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

ans = 1e9


def chk_range(a, b, c, d):
    if a + c + d >= N:
        return False
    if b - c < 0:
        return False
    if b + d >= N:
        return False
    return True


def chk_population(a, b, c, d):
    people = [0, 0, 0, 0, 0]
    for i in range(N):
        for j in range(N):
            if 0 <= i < a + c and 0 <= j < b:
                people[0] += A[i][j]
            if 0 <= i <= a + d and b < j < N:
                people[1] += A[i][j]
            if a + c <= i < N and 0 <= j < b - c + d:
                people[2] += A[i][j]
            if a + d < i <= N and b - c + d <= j < N:
                people[3] += A[i][j]
            people[4] += A[i][j]

    for i in range(4):
        people[4] -= people[i]

    return max(people) - min(people)


for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if chk_range(x, y, d1, d2):
                    if ans > chk_population(x, y, d1, d2):
                        ans = chk_population(x, y, d1, d2)

print(ans)