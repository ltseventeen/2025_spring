lines = []
while True:
    try:
        line = input()
        if line:  # 如果输入非空，则添加到列表中
            lines.append(line)
        else:  # 遇到空行则停止读取
            break
    except EOFError:  # 当用户输入 EOF (Ctrl+D on Unix, Ctrl+Z on Windows) 时退出循环
        break

for line in lines:
    stack=[]
    mark=[]
    for i in range(len(line)):
        if line[i]=='(':
            stack.append(i)
            mark.append(' ')
        elif line[i]==')':
            if not stack:
                mark+='?'
            else:
                mark+=' '
                stack.pop()
        else:
            mark+=' '

    while stack:
        mark[stack[-1]]='$'
        stack.pop()

    print(line)
    print(''.join(map(str,mark)))