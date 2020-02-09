# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        tail = head
        n = 1
        while tail.next:
            n += 1 
            tail = tail.next
        tail.next = head

        cur_tail = head
        for i in range(n - k % n - 1):
            cur_tail = cur_tail.next
        cur_head = cur_tail.next
        cur_tail.next = None
        return cur_head
        