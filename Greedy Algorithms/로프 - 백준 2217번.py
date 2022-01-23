import sys
sys.stdin = open('in12.txt', 'rt')
n = int(input())
rope = [int(sys.stdin.readline()) for i in range(n)]
rope.sort()
result = 0
for i in range(n):
    if result < n * rope[i]:
        result = n * rope[i]
        n -= 1
    else:
        n -= 1
print(result)


# n = int(input())
# a = int(input())
# b = int(input())
# result = 0
#
# for i in range(n):
#     if a<b:
#         result += a
#     else:
#         result += b
# print(result)
