import sys
sys.stdin = open('in7.txt','rt')
n,k=map(int,input().split())
coin=[]
result = 0
for i in range(n):
    num = int(input())
    coin.append(num)
    coin.sort(reverse=True)

for i in coin:
    if k == 0:
        break
    result+=k//i
    k%=i
print(result)
