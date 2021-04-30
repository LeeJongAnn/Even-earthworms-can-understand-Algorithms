import sys
sys.stdin = open('in5.txt', 'rt')

n = int(input())
k = list(map(int,input().split()))


def digit_sum(x):
    res = 0
    while x>0 :
        res += x % 10
        x = x // 10
    print(res)

for x in k:
    total= digit_sum(x)
    print(total,end = ' ')