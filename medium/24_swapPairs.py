# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = ListNode(-1)
        p.next, a = head, p
        while a.next and a.next.next:
            l,r = a.next, a.next.next
            r = a.next.next
            l.next = r.next
            r.next = l
            a.next = r
            a = l
        return p.next