import sys
sys.stdin = open('in21.txt','rt')

a = list(input())
tmp = []
cnt = 0
print(a)
for i in range(len(a)):
    tmp.append(a[i])
    if tmp[i] == "0":
        tmp[i] = "1"
    else:
        tmp[i] = "0"
        if tmp[i] == "0":
            tmp[i] = "1"
            cnt +=1
print(tmp)
print(cnt)