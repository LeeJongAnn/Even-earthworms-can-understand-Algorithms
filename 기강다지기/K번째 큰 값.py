import sys
sys.stdin = open("in3.txt", "rt")

n,k = map(int,input().split())
a = list(map(int,input().split()))
res = set()

for i in range(1,n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            result = a[i]+a[j]+a[m]
            res.add(result)
            res_new = list(res)
            res_new.sort(reverse=True)
print(res_new[k-1])