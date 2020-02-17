from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        level = 0
        queue = deque([root, ])
        while queue:
            levels.append([])
            lens = len(queue)
            for i in range(lens):
                node = queue.popleft()
                if level % 2 == 0:
                    levels[level].append(node.val)
                else:
                    levels[level].insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return levels