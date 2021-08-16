import sys
sys.stdin = open('in9.txt','rt')

n = int(input())
num = list(map(int, input().split()))
waiting = []
num.sort()
results = 0

for i in range(n):

    results += num[i]
    waiting.append(results)

sum = 0
for j in waiting:

    sum+= j

print(sum)
