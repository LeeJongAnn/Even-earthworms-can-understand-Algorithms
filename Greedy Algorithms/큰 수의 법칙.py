import sys
sys.stdin = open("in16.txt","rt")

a,b,c = map(int,input().split())
num = list(map(int,input().split()))

num.sort(reverse=True)

first = num[0]
second = num[1]
result = 0
print(num)

while True:
    for i in range(c):
        if b == 0:
            break
        result += first
        b -=1
    if b == 0:
        break
    result += second
    b -= 1
print(result)