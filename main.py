import sys
sys.stdin = open("in1.txt", "rt")

n = int(input())

a = list(map(int, input().split()))
sum = 0
average = 0
for i in range(n):
    sum += a[i]

result = sum // n


if result == a[i]:
    print(a[i])
else:
    print(-1)

