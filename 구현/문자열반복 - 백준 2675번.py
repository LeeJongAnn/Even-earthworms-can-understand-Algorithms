import sys
import time
start = time.time()
sys.stdin = open("in22.txt", 'rt')

n = int(input())

tmp = []

for _ in range(n):
    a,b = input().split()
    for j in range(0,int(a)-1):
        tmp.append(b[j]*int(a))
print(tmp)
