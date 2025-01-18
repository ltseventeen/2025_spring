class CircleLinkList:
    class Node:
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.tail = None  # 尾指针，指向最后一个节点
        self.size = 0  # 链表大小

    def is_empty(self):
        """检查链表是否为空"""
        return self.size == 0

    def pushFront(self, data):
        """在链表头部插入元素"""
        nd = CircleLinkList.Node(data)
        if self.is_empty():
            self.tail = nd
            nd.next = self.tail  # 自己指向自己形成环
        else:
            nd.next = self.tail.next  # 新节点指向当前头节点
            self.tail.next = nd  # 当前尾节点指向新节点
        self.size += 1

    def pushBack(self, data):
        """在链表尾部插入元素"""
        nd = CircleLinkList.Node(data)
        if self.is_empty():
            self.tail = nd
            nd.next = self.tail  # 自己指向自己形成环
        else:
            nd.next = self.tail.next  # 新节点指向当前头节点
            self.tail.next = nd  # 当前尾节点指向新节点
            self.tail = nd  # 更新尾指针
        self.size += 1

    def popFront(self):
        """移除并返回链表头部元素"""
        if self.is_empty():
            return None
        else:
            old_head = self.tail.next
            if self.size == 1:
                self.tail = None  # 如果只有一个元素，更新尾指针为None
            else:
                self.tail.next = old_head.next  # 跳过旧头节点
            self.size -= 1
            return old_head.data

    def popBack(self):
        """移除并返回链表尾部元素"""
        if self.is_empty():
            return None
        elif self.size == 1:
            data = self.tail.data
            self.tail = None
            self.size -= 1
            return data
        else:
            prev = self.tail
            while prev.next != self.tail:  # 找到倒数第二个节点
                prev = prev.next
            data = self.tail.data
            prev.next = self.tail.next  # 跳过尾节点
            self.tail = prev  # 更新尾指针
            self.size -= 1
            return data

    def printList(self):
        """打印链表中的所有元素"""
        if self.is_empty():
            print('Empty!')
        else:
            ptr = self.tail.next
            while True:
                print(ptr.data, end=', ' if ptr != self.tail else '\n')
                if ptr == self.tail:
                    break
                ptr = ptr.next

    def remove(self, data):
        if self.size == 0:
            return

        ptr = self.tail
        while ptr.next.data != data:
            ptr = ptr.next
            if ptr == self.tail:
                return

        self.size -= 1
        if ptr.next == self.tail:
            ptr.next = self.tail.next
            self.tail = ptr
        else:
            ptr.next = ptr.next.next
        return


def find_king(n,m):
    clist=CircleLinkList()
    used=[False]*(n+1)
    for i in range(1,n+1):
        clist.pushBack(i)

    temp=1
    ptr=clist.tail.next
    while clist.size>1:
        if temp==m:
            clist.remove(ptr.data)
            ptr=ptr.next
            temp=1
            continue

        temp+=1
        ptr=ptr.next
    clist.printList()

while True:
    n,m=map(int,input().split())
    if n==m==0:
        break

    find_king(n,m)