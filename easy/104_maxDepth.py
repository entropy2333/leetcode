# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if not root:
            return 0
        return self.getDepth(root, depth)

    def getDepth(self, root, depth):
        depth += 1
        if not root.left and not root.right:
            return depth
        if not root.left:
            return self.getDepth(root.right, depth)
        if not root.right:
            return self.getDepth(root.left, depth)
        return max(self.getDepth(root.left, depth), self.getDepth(root.right, depth))

        return max(self.getDepth(left, depth), self.getDepth(right, depth))