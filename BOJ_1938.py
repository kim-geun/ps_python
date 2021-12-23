# # https://www.acmicpc.net/problem/1938
#
# from collections import deque
# from sys import stdin
#
# input = stdin.readline()
#
# dx, dy = [1, -1, 0, 0, 1, 1, -1, -1], [0, 0, -1, 1, -1, 1, -1, 1]
#
# n = int(input())
# s = []
# b = deque()
# e = deque()
# vis = [[[0 for _ in range(2)] for _ in range(n)] for _ in range(n)]
#
# for i in range(n):
#     a = list(input().strip())
#     s.append(a)
#     for j in range(n):
#         if a[j] == 'B': b.append([i, j])
#         if a[j] == 'E': e.append([i, j])
# if b[1][1] - b[0][1] == 1:b.append([b[1][0],b[0][0],0,0])
# else: b.append([b[1][0],b[0][0],1,0])
# if a[1][1] - a[0][1] == 1:a.append([a[1][0],a[0][0],0,0])
# else: a.append([a[1][0],a[0][0],1,0])
#
# def chk(x, y):
#     for i in range(8):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= nx
