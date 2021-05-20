import sys

sys.stdin = open("in6.txt","rt")

n = int(input())

a = [list(map(int , input().split())) for _ in range(n)]

largetst = -214700000

for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largetst:
        largetst = sum1
    if sum2>largetst:
        largetst = sum2

sum1=sum2=0

for i in range(n):

    sum1+=a[i][i]
    sum2+=a[i][n-i-1]

    if sum1>largetst:
        sum1=largetst
    if sum2>largetst:
        sum2=largetst
print(largetst)
