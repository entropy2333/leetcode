# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        pre, nxt = head, head.next
        while nxt.next:
            if pre == nxt:
                return True
            pre = pre.next
            nxt = nxt.next
        return False