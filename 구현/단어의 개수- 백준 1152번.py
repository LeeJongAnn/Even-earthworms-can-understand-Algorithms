import sys
sys.stdin = open("in15.txt", "rt")
n = input().split(' ')
print(n)
count = 0
tmp = []
for i in range(len(n)):
    count += 1
    if n[i] == '':
        count -= 1
print(count)
