# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.compare(root.left, root.right)
    
    def compare(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if not root1.val == root2.val:
            return False
        return (True and self.compare(root1.left, root2.right) and self.compare(root1.right, root2.left))