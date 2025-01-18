# 判断是否为数字
def is_number(s):
    try:    # 如果能运⾏ float(s) 语句，返回 True（字符串 s 是浮点数）
        float(s)
        return True
    except ValueError:  # ValueError 为 Python 的⼀种标准异常，表⽰"传⼊⽆效的参数"
        pass  # 如果引发了 ValueError 这种异常，不做任何事情（pass：不做任何事情，⼀般⽤做占位语句）
    try:
        import unicodedata  # 处理 ASCII 码的包
        unicodedata.numeric(s)  # 把⼀个表⽰数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError, ValueError):
        pass
        return False

n=int(input())
for _ in range(n):
    str_in=list(input().split())

    num=[]
    for i in str_in:
        if is_number(i):
            num.append(float(i))
        else:
            if i=='+':
                b=num.pop()
                a=num.pop()
                op=a+b
                num.append(op)
            elif i=='-':
                b = num.pop()
                a = num.pop()
                op = a - b
                num.append(op)
            elif i=='*':
                b = num.pop()
                a = num.pop()
                op = a * b
                num.append(op)
            elif i=='/':
                b = num.pop()
                a = num.pop()
                op = a / b
                num.append(op)
    result=num[0]
    print(f'{result:.2f}')