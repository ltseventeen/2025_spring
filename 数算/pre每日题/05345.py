def C(d):
    for index,num in enumerate(l):
        #print(index,num)
        num=(num+d)%65536
        l[index]=num
    return

def Q(i):
    cnt=0
    for num in l:
        bin_num=int(bin(num)[2:])
        if (bin_num>>i)&1:
            cnt+=1
    return cnt


n,m=map(int,input().split())
l=list(map(int,input().split()))
for _ in range(m):
    move=list(input().split())
    if move[0]=='C':
        d=int(move[1])
        C(d)
        #print(l)
    elif move[0]=='Q':
        i=int(move[1])
        print(Q(i))