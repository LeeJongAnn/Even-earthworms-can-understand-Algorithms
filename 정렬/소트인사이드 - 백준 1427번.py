import sys
sys.stdin = open("in4.txt", 'rt')
n = input()
print(n)
tmp = []
for x in n:
    tmp.append(int(x))
print(tmp)
tmp.sort(reverse=True)
for x in tmp:
    print(x,end="")

