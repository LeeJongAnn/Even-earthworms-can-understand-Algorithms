import sys
sys.stdin = open("11.txt",'rt')
n = (input())
tmp = []
left = 0
right = 0
cnt = 0
for i in range((len(n)//2)):
    left += int(n[i])
print(left)

for i in range((len(n)//2)):
    left -= int(n[i])
print(left)

if left == 0:
    print("LUCKY")
else:
    print("READY")