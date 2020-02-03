# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 自顶向下
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.getDepth(root.left) - self.getDepth(root.right)) < 2
    
    def getDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))

# 自底向上
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.getDepth(root) == -1:
            return False
        else:
            return True
    
    def getDepth(self, root):
        if not root:
            return 0
        left = self.getDepth(root.left)
        if left == -1:
            return -1
        right = self.getDepth(root.right)
        if right == -1:
            return -1
        if abs(left - right) < 2:
            return 1 + max(left, right)
        else:
            return -1