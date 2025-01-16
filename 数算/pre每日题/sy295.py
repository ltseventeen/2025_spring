#可能的出栈序列
#先生成所有可能的排列，然后检验他们是否合法
n=int(input())

def is_valid(n,pop_s):
    s=[]
    j=0
    for i in range(1,n+1):
        s.append(i)
        while s and s[-1]==pop_s[j]:
            s.pop()
            j+=1
    return True if not s else False

answer=[]
used=[False]*(n+1)
temp=[]
def dfs(index):
    if index==n+1:
        if is_valid(n,temp):
            answer.append(temp[:])
            print(' '.join(map(str,temp)))
            return

    for i in range(1,n+1):
        if not used[i]:
            used[i]=True
            temp.append(i)
            dfs(index+1)
            used[i]=False
            temp.pop()

dfs(1)