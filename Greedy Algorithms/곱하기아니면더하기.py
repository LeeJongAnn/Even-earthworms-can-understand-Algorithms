import sys
sys.stdin = open("in20.txt","rt")

num = input()
num = list(num)

num.sort()
result = 0
first = int(num[0])
second = int(num[1])
cnt = 0
for i in range(len(num)-1):
    if i == 0:
        result = first + second
        cnt+=1
    elif i >=1:
        result += int(num[i]) * int(num[i+1])
        cnt+=1
print(result)
print(cnt)