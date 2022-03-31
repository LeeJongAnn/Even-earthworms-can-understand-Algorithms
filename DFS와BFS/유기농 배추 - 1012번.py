import sys
from collections import deque
sys.stdin = open("in14.txt","rt")
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y,data):
    q = deque()
    q.append((x,y))
    data[x][y] = value
    count[value] = 1

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0>=nx or 0>=ny or ny>n or nx>n:
                continue
            if data[nx][ny] == value or data[nx][ny] == 0:
                continue
            data[nx][ny] = value
            count[value] += 1
    return

value = 2
count = {}


t = int(input())
for _ in range(t):
    a,b,c = map(int,input().split())
    data = [[0] * b for _ in range(a)]

    for _ in range(a):
        x,y = map(int,input().split())
        data[x][y] = 1

    for i in range(b):
        for j in range(a):
            if data[i][j] == 1:
                bfs(i,j,data)


