import sys
import time
start = time.time()
sys.stdin = open("in16.txt","rt")
a,b,c= map(int,input().split())
print(a,b,c)
num = list(map(int,input().split()))
print(num)
num.sort(reverse=True)
MostLarge = num[0]
SecondLarge = num[1]
print(MostLarge)
print(SecondLarge)
result = 0
count = 0
count2 = 0
while True:
    for i in range(c):
        if b == 0:
            break
        b -= 1
        result += MostLarge
        count +=1
    if b == 0:
        break
    b -=1
    result += SecondLarge
    count2 += 1
print(result)
print("큰 수는:" ,count,"작은 수는:",count2)
print("걸린 시간:" ,time.time() - start)
