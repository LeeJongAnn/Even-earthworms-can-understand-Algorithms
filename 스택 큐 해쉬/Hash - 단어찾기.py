import sys
sys.stdin = open("in6.txt", "rt")
k = int(input())
p = dict()
for i in range(k):

    word= input()
    p[word]=1

for i in range(k-1):

    word = input()
    p[word] = 0

for key,val in p.items():
    if val == 1:
        print(key)
        break