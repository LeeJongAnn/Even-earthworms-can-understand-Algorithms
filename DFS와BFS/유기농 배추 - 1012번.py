import sys
from collections import deque
sys.stdin = open("in14.txt","rt")
dx = [0,0,1,-1]
dy = [1,-1,0,0]

t = int(input())
data = []
a,b,c = map(int,input().split())
data = [[0] * b for _ in range(a)]
for i in range(c):
    x,y = map(int,input().split())
    data[x][y] = 1

for q in data:
    print(q)