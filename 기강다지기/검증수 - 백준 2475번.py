import sys
sys.stdin = open("in7.txt", "rt")

a = list(map(int,input().split()))
result = 0
for i in a:
    result += i*i
final = result % 10
print(final)