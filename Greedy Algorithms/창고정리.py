import sys
sys.stdin = open("in3.txt", "rt")

L = int(input())
m = list(map(int,input().split()))
num = int(input())
print(m)
m.sort()
print(m)
result = 0
for i in range(num):
    m[0]+=1
    m[-1]-=1
    m.sort()
    result = m[-1] - m[0]
print(result)


