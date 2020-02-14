class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

# 统计树中节点
def countNode(root):
    if not root:
        return 0
    else:
        return 1 + countNode(root.left) + countNode(root.right)

# 求二叉树里所有数值和
def sumNode(root):
    if not root:
        return 0
    else:
        return root.data + sumNode(root.left) + sumNode(root.right)

# 前序遍历
def preOrder(root):
    if not root:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# 中序遍历
def midOrder(root):
    if not root:
        return

    midOrder(root.left)
    print(root.data, end=' ')
    midOrder(root.right)

# 后序遍历
def postOrder(root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end=' ')

# 非递归实现前序遍历
def preOrderNonRec(Node):
    if not Node:
        return
    #用数组当栈
    stack = []
    while Node or stack:
        while Node:
            # 从根节点开始，一直找它的左子树
            print(Node.data, end=' ')
            #将右子树压入栈中
            stack.append(Node)
            #一直往下找左子树
            Node = Node.left
        # while结束表示当前节点Node为空，即前一个节点没有左子树了
        # 栈中开始弹出上右子树，再重复前面步骤
        Node = stack.pop()
        Node = Node.right

# 非递归实现中序遍历
# 中序的非递归遍历与先序的非递归遍历类似。先序遍历是先访问节点，然后再将节点入栈，
# 后中序遍历则是先入栈，然后节点弹出栈后再访问。
def midOrderNonRec(Node):
    if not Node:
        return
    #用数组当栈
    stack = []
    while Node or stack:
        while Node:
            # 从根节点开始，一直找它的左子树
            # 将父节点压入栈中
            stack.append(Node)
            # 一直往下找左子树
            Node = Node.left
        # while结束表示当前节点Node为空，即前一个节点没有左子树了
        # 栈中开始弹出，再重复前面步骤
        Node = stack.pop()
        print(Node.data, end=' ')
        Node = Node.right

# 非递归实现后序遍历
def postOrderNonRec(Node):
    if not Node:
        return
    # 用数组当栈
    stack = []
    while Node or stack:
        while Node:
            # 从根节点开始，一直找它的左子树
            stack.append(Node)
            # 能左就左，否则就向右走一步
            Node = Node.left if Node.left else Node.right

        # 到下面都没有左子树和右子树的节点后，栈中开始弹出

        Node = stack.pop() # 栈顶就是当前应访问节点
        print(Node.data, end=' ')
        # 栈不空且当前节点是栈顶的左子节点，那么应当继续去访问栈顶的右子节点
        if len(stack) > 0 and stack[-1].left == Node:
            Node = stack[-1].right
        else:
            # 没有右子树或右子树遍历完毕，强迫退栈
            Node = None

# 广度优先搜索算法
def BFS(root):
    if not Node:
        return
    quene = []
    quene.append(root)
    while quene:
        root = quene.pop(0)
        print(root.data, end=' ')
        if root.left:
            quene.append(root.left)
        if root.right:
            quene.append(root.right)

# 深度优先搜索算法
def DFS(root):
    stack = []
    stack.append(root)
    while stack:
        root = stack.pop()
        print(root.data, end=' ')
        if root.right:
            stack.append(root.right)
        if root.left:
            stack.append(root.left)
 
if __name__ == '__main__':
    t = Node(1, Node(2, Node(3), Node(4)), Node(5))
    # 统计树中节点
    print("count: {}".format(countNode(t)))
    # 求二叉树里所有数值和
    print("sum: {}".format(sumNode(t)))
    # 前序遍历
    # preOrder(t)
    # # 中序遍历
    # midOrder(t)
    # # 后序遍历
    # postOrder(t)
    print("preOrder:")
    preOrderNonRec(t)
    print("\nmidOrder:")
    midOrderNonRec(t)
    print("\npostOrder:")
    postOrderNonRec(t)
    print("\nBFS:")
    BFS(t)
    print("\nDFS:")
    DFS(t)