import sys
sys.stdin = open("in1.txt", 'rt')
n = int(input())
result =0
cnt =0
while n>3:
    while n%3!=0:
        n -= 1
        cnt +=1
        n//=3
        cnt +=1
    while n%2!=0:
        n -=1
        cnt +=1
        n//=2
        cnt +=1
    if n%3!=0 and n%2!=0:
        n -= 1
        cnt +=1
print(cnt)