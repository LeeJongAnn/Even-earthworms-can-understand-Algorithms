import sys

sys.stdin = open("in2.txt", "rt")

T = int(input())
res = set()

for i in range(T):
    n, s, e, k = map(int, input().split())
    a = list(map(int, input().split()))

    res= a[s-1:e]
    res.sort()
    print("#%d %d" %(i+1,res[k-1]))