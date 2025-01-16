n=int(input())
s=[]
pop_s=list(map(int,input().split()))

def is_valid(n):
    j=0
    for i in range(1,n+1):
        s.append(i)
        while s and s[-1]==pop_s[j]:
            s.pop()
            j+=1
    return True if not s else False

if is_valid(n):
    print('Yes')
else:
    print('No')