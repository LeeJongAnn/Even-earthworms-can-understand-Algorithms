import sys
sys.stdin = open('in6.txt','rt')

n = int(input())
m = list(map(int,input().split()))
seq = [0] * n
cnt = 0
for i in range(n):
    for j in range(n):
        if m[i] == 0 and seq[j] == 0:
            seq[j] = i + 1
            break
        elif seq[j] == 0:
            m[i] -= 1
for x in seq:
    print(x,end=" ")
