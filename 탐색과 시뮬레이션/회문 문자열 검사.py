import sys
sys.stdin = open("in8.txt", "rt")
n = int(input())


for i in range(n):

    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):

        if s[j]==s[-j-1]:
            print("YES")
        else:
            print("NO")





