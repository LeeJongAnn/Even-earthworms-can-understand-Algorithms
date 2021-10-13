import sys
sys.stdin = open('in6.txt','rt')

def DFS(v):

    if v == s+1:
        for i in range(1,s+1):
            if ch[i] == 1:
                print(i,end= " ")
            print()
    else:
        ch[v] = 1
        DFS(v+1)
        ch[v] = 0
        DFS(v+1)

if __name__ == "__main__":
    s,e = map(int,input().split())
    a = list(map(int,input().split()))
    ch = [0] * (s+1)
    DFS(5)
