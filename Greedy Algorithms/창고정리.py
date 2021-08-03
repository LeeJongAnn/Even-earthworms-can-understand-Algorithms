import sys
sys.stdin = open("in3.txt", "rt")

L = int(input())
num = list(map(int,input().split()))
time = int(input())
num.sort()


for _ in range(time):

    num[0] += 1
    num[-1] -= 1
    num.sort()

print(num[L-1] - num[0])
