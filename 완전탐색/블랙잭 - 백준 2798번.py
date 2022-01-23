import sys
sys.stdin = open('in6.txt','rt')

def DFS(L,sum):
    if sum>e:
        return
    global result
    if L == s:
        if sum>result:
            result = sum
    else:
        DFS(L+1,sum+a[L])
        DFS(L+1,sum)


if __name__ == "__main__":
    s,e = map(int,input().split())
    a = list(map(int,input().split()))
    result = 0
    ch = [0] * s
    DFS(0,0)
    print(result)
