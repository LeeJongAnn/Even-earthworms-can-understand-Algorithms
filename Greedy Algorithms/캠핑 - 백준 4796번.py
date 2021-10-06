import sys
sys.stdin = open("in15.txt", "rt")

l,p,v = map(int ,input().split())

count = int(v//p)
intro = int(v%p)
result = (count * l) + intro

count2 = int(v//p)
intro2 = int(v%p)
result2 = (count2 * l) + intro
print("Case 1: " + str(result))
print("Case 2: " + str(result2))
