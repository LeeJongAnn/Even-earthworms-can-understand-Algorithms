import sys
sys.stdin = open("in23.txt", "rt")

s,e = map(int,input().split())
num = list(map(int,input().split()))
weight_list = [0]*(e+1)

for weight in num:
    weight_list[weight] += 1
cnt = 0

for i in range(1,e+1):
    s -= weight_list[i]
    cnt += weight_list[i] * s
print(cnt)