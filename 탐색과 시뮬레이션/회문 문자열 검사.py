import sys

sys.stdin = open("in8.txt", "rt")
n = int(input())

for i in range(0,n):
    s = input()
    s = s.upper()
    size = len(s)

    for j in range(size // 2):

        if s[j] != s[-1-j]:
            print("No")
            break
    else:
       print("YES")
