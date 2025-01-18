#第一个数保留，后面的数字和符号交换顺序即可
l=list(input().split())
lenth=len(l)
answer=[]
answer.append(l[0])
for i in range(1,lenth,2):
    symbol=l[i]
    num=l[i+1]
    answer.append(num)
    answer.append(symbol)

print(' '.join(map(str,answer)))