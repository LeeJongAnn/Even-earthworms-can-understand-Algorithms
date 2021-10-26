import sys
sys.stdin = open("in26.txt","rt")

a = 300
a1 = 0
b = 60
b2 = 0
c = 10
c2 = 0
n = int(input())
result = 0

if n>a:
    result = n%a
    a1 +=1
else:
    result = n%b
    if result<b:
        b2 +=1
        result = result%c
        if result < c:
            c2 += 1
print(a1,b2,c2)