import sys
sys.stdin = open("in8.txt", "rt")
n,k = map(int,input().split())
num = list(map(int,input().split()))
tmp = []
for x in num:
    if x<k:
       print(x,end=" ")