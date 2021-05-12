import sys
sys.stdin = open("in6.txt", "rt")

k = int(input())

cnt = [0] * (k+1)


for n in range(1,k+1,k):

    if n % k == 0:
        cnt[n] += 1
        print(cnt[n])
