# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        p = ListNode(-1)
        p.next = head

        pre = head
        cur = head
        flag = True
        while cur.next:
            # [1, 2, 2, 3, 4, 4, 5, 6, 7]
            # print(pre.val, cur.val)
            if cur.next.val == cur.val:
                cur = cur.next
                flag = False
                continue
            if p.next.val == cur.val and not flag:
                flag = True
                p.next = cur.next
                pre = cur = p.next
            elif flag:
                pre, cur = cur, cur.next
            else:
                flag = True
                pre.next = cur.next
                cur = cur.next
        return p.next
