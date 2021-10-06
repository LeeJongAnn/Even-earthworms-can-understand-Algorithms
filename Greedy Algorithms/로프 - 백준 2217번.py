import sys
sys.stdin = open('in12.txt','rt')

n = int(input())
a = int(input())
b = int(input())
result = 0
if a<b:
    result = a*2
else:
    result = b*2

print(result)