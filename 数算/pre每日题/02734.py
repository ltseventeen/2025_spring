#十进制转八进制
a=int(input())
stack=[]
while a:
    stack.append(a%8)
    a//=8

answer=[]
while stack:
    answer.append(stack.pop())
print(''.join(map(str,answer)))