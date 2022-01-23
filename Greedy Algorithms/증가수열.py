import sys
sys.stdin = open("in5.txt", "rt")
n = int(input())
num = list(map(int,input().split()))
lt = 0
rt = n-1
last = 0
tmp = []
res = ""
while lt<=rt:
    if num[lt]>last:
        tmp.append((num[lt],'L'))
    if num[rt]>last:
        tmp.append((num[rt],'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res = res + tmp[0][1]
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
    tmp.clear()
print(res)
print(len(res))
