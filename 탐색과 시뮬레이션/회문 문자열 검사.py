import sys
sys.stdin = open("in8.txt", "rt")
n = int(input())

for i in range(0,n):

    s = input()
    s = s.upper()
    size = len(s)
    for m in range(size//2):

        if s[m]!=s[-1-m]:
            print("# %d NO" %(i+1))
            break
    else:
         print("# %d YES" %(i+1))