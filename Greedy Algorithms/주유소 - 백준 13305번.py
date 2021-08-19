import sys
sys.stdin = open("in10.txt",'rt')

n = int(input())

length = list(map(int,input().split()))
oil_price = list(map(int,input().split()))
res = ''
tmp = []


for i in range(n):

    if len(length)<len(oil_price):
        tmp.append((length[i],oil_price[i]))
    print(tmp)