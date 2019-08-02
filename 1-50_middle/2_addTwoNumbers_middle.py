# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 60ms
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        elif l1.val + l2.val < 10:
            l1.val += l2.val
            l1.next = self.addTwoNumbers(l1.next, l2.next)
            return l1    
        elif l1.val + l2.val >= 10:
            l1.val = (l1.val + l2.val)%10
            l1.next = self.addTwoNumbers(l1.next, ListNode(1))
            l1.next = self.addTwoNumbers(l1.next, l2.next)
            return l1