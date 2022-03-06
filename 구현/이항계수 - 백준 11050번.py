from collections import deque
from itertools import combinations
import sys
sys.stdin = open("in20.txt", 'rt')

n,k = map(int,input().split())
numList = []
for i in range(1,n+1):
    numList.append(i)

result= list(combinations(numList,k))
cnt = 0
for _ in range(len(result)):
    cnt += 1
print(cnt)