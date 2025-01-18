class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next

class LinkList:
    def __init__(self):
        self.head = None

    def initList(self, data):
        self.head = Node(data[0])
        p = self.head
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def insertCat(self):
        #直接算长度找中点
        length=len(lst)
        #插入位置（第p个数后面）
        if length%2==0:
            p=length//2
        else:
            p=length//2+1

        #移动指针到插入位置
        index=self.head
        for _ in range(p-1):
            index=index.next
        node=Node(data=6,next=index.next)
        index.next=node

    def printLk(self):
        p = self.head
        while p:
            print(p.data, end=" ")
            p = p.next
        print()

lst = list(map(int,input().split()))
lkList = LinkList()
lkList.initList(lst)
lkList.insertCat()
lkList.printLk()