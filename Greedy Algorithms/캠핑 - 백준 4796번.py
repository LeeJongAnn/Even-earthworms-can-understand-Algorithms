import sys
sys.stdin = open("in15.txt", "rt")

s,e,q = map(int,input().split())
count = q // e
moduler = q % e
result = 0
for i in range(count):
    result += s
if moduler<=s:
    result +=moduler
print("Case1: " + str(result))

s2,e2,q2 = map(int,input().split())
count2 = q2 // e2
moduler2 = q2 % e2
result2 = 0
for i in range(count2):
    result2 += s2
if moduler2<=s2:
    result2 +=moduler2
print("Case2: " + str(result2))
