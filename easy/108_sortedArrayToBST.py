# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])

        left = nums[:mid]
        right = nums[mid+1:]

        node.left = self.sortedArrayToBST(left)
        node.right = self.sortedArrayToBST(right)

        return node
