while True:
    n,k=map(int,input().split())
    if n==-1 and k==-1:
        break
    desk=[]
    for _ in range(n):
        desk.append(list(input()))

    cnt=0
    placed=[False]*10  #每一列有没有放过棋子
    def dfs(q,p):  #q表示当前行数，p表示当前摆放棋子号（从0开始）
        global cnt
        if p==k:
            cnt+=1
            return
        if q==n:
            return

        #遍历当前及以后的行,i行j列
        for i in range(q,n):
            for j in range(n):
                if desk[i][j]=='#' and not placed[j]:
                    placed[j]=True
                    dfs(i+1,p+1)
                    placed[j]=False

    dfs(0,0)
    print(cnt)