n=int(input())
l=[]
for _ in range(n):
    a=list(input().split())
    if a[0]=='push':
        l.append(int(a[1]))
    elif a[0]=='pop':
        if l:
            print(l.pop())
        else:
            print(-1)