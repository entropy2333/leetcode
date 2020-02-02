# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        value = []
        value.append([root.val])
        child = self.getChild([root])
        while child:
            value.append(self.getValue(child))
            child = self.getChild(child)
        return value[::-1]

    def getChild(self, root):
        def getchild(root):
            l = []
            if root.left:
                l.append(root.right)
            if root.right:
                l.append(root.left)
        child = []
        for node in root:
            if node:
                child.extend(getchild(node))
        return child

    def getValue(self, root):
        def getvalue(root):
            return [root.val]
        value = []
        for node in root:
            if node:
                value.extend(getvalue(node))
        return value
