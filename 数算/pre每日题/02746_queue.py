from collections import deque
def find_king(n,m):
    queue=deque()
    for i in range(1,n+1):
        queue.append(i)
    while len(queue)>1:
        for _ in range(1,m):
            queue.append(queue.popleft())
        queue.popleft()
    print(queue[0])

while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    find_king(n,m)