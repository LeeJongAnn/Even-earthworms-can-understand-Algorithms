import sys
sys.stdin = open('in12.txt','rt')

n = int(input())
tmp = []
results  = 0
for i in range(n):
    L = int(input())
    tmp.append(L)
    tmp.sort()
    if tmp[i]<tmp[i+1]:
        results = tmp[i]*2
print(results)
