import sys
sys.stdin = open("in10.txt", 'rt')

n = input()
num = input()
result = 0
for i in range(len(num)):
    result +=int(num[i])
print(result)