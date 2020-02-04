# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p = ListNode(-1)
        p.next, a, b = head, p, p
        
        while n > 0 and b:
            b = b.next
            n -= 1
        if not b:
            return head
        while b.next:
            a = a.next
            b = b.next
        a.next = a.next.next
        return p.next