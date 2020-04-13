class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class binaryTree(object):
    def __init__(self, value):
        self.root = Node(value)

    def heightOfTree(self, node):
        if node is None:
            return -1
        leftNode = self.heightOfTree(node.left)
        # print(leftNode)
        rightNode = self.heightOfTree(node.right)
        return 1 + max(leftNode, rightNode)


tree = binaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.heightOfTree(tree.root))