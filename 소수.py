import sys
sys.stdin = open("in6.txt", "rt")

n = int(input())
cnt = 0

ch = [0] * (n+1)
for i in range(2,n+1):


    for j in range(i,n+1,i):
        if ch[j] == 0 :
            cnt+=1
            print(ch[j],end=" ")




