from collections import deque
import sys
sys.stdin = open("in5.txt", 'rt')
n = int(input())
temp = []
for i in range(n):
    a,b = map(int,input().split())
    temp.append((a,b))
temp.sort()

for x,y in temp:
    print(x,y)