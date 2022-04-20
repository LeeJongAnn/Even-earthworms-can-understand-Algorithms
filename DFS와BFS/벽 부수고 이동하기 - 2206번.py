import sys
from collections import deque
sys.stdin = open("in20.txt", 'rt')

n,k = map(int,input().split())
print(n,k)

graph = [[0] * k for _ in range(n)]
temp = []
for _ in range(n):
    temp.append(list(map(int,input().strip())))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def move(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx or nx<n or 0<=ny or ny<k:
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2

def get_score():
    score = 0
    for i in range(n):
        for j in range(k):
            if graph[i][j] == 0:
                score += 1
    return
result = 0
def simulate(count):
    global result
    if count == 1:
        for i in range(n):
            for j in range(k):
                graph[i][j] = temp[i][j]
        for i in range(n):
            for j in range(k):
                if graph[i][j] == 0:
                    move(i,j)
        result = max(result,get_score())
    return
