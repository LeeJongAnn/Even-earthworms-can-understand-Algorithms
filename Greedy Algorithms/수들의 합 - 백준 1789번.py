import sys
sys.stdin = open("in25.txt","rt")
n = int(input())
result = 0
tmp = []
cnt = 0
for i in range(1,50):
    if result<=200:
        result += i
        tmp.append(i)
        cnt +=1
    else:
        break
print(result)
print(cnt)
print(tmp)