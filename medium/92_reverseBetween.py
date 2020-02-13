# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        # Move the two pointers until they reach the proper starting point
        # in the list.
        cur, pre = head, None
        while m > 1:
            pre = cur
            cur = cur.next
            m, n = m - 1, n - 1

        # The two pointers that will fix the final connections.
        tail, con = cur, pre

        # Iteratively reverse the nodes until n becomes 0.
        while n:
            third = cur.next
            cur.next = pre
            pre = cur
            cur = third
            n -= 1

        # Adjust the final connections as explained in the algorithm
        if con:
            con.next = pre
        else:
            head = pre
        tail.next = cur
        return head