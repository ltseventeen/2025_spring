# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #特殊情况处理
        if not head or not head.next:
            return True

        #利用快慢指针找到链表中点
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #反转后面一半链表
        pre=None
        current=slow
        while current:
            next_node=current.next
            current.next=pre
            pre=current
            current=next_node

        #比较前后两部分是否一致
        left,right=head,pre
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next

        return True