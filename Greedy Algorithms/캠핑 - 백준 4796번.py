import sys

sys.stdin = open("in15.txt", "rt")

count = 1
while True:
    L, P, V = map(int, input().split())

    if L == 0 & P == 0 & V == 0:
        break;

    num, rest = divmod(V, P)

    result = num * L + (L if rest > L else rest)

    print("Case " + str(count) + ":", result)
    count += 1
# 이래도 안풀려???
# 부족한 실력에 좌절을 .....
# n,p,q = map(int,input().split())
# s,e,u = map(int,input().split())
# cnt = 0
# cnt2 = 0
# loop = q // p
# moduler = q % p
# for i in range(p):
#     if n == 0:
#         break
#     n -= 1
#     cnt +=1
# result = cnt * loop + moduler
# print("Case 1:",result)
#
# loop2 = u // e
# moduler2 = u % e
# for j in range(e):
#     if s == 0:
#         break
#     s -= 1
#     cnt2 += 1
# result2 = cnt2 * loop2 + moduler2
# print("Case 2:", result2)

# s,e,q = map(int,input().split())
# count = q // e
# moduler = q % e
# result = 0
# for i in range(count):
#     result += s
# if moduler<=s:
#     result +=moduler
# print("Case1: " + str(result))
#
# s2,e2,q2 = map(int,input().split())
# count2 = q2 // e2
# moduler2 = q2 % e2
# result2 = 0
# for i in range(count2):
#     result2 += s2
# if moduler2<=s2:
#     result2 +=moduler2
# print("Case2: " + str(result2))
