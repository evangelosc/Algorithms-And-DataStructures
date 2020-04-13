class Queue(object):
    def __init__(self):
        self.items = list()

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()   

    def peek(self):
        if not self.isEmpty():
            return self.items[-1].value

    def isEmpty(self):
        return len(self.items)==0

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)



class Node(object):
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class binaryTree(object):
    def __init__(self, value):
        self.root = Node(value)

    def helperPrint(self, traversalType):
        if traversalType == "preorder":
            print("Preorder Traversal")
            return self.preorderPrint(tree.root, "")
        elif traversalType == "inorder":
            print("Inorder Traversal")
            return self.inorderPrint(tree.root, "")
        elif traversalType == "postorder":
            print("Postorder Traversal")
            return self.postorderPrint(tree.root, '')
        elif traversalType == "levelorder":
            print("Levelorder Traversal")
            return self.levelorderPrint(tree.root)
        elif traversalType == "reverseorder":
            print("Reverse Order Traversal")
            return self.reverseorderPrint(tree.root)
        elif traversalType == "heightoftree":
            print("The height of the tree is")
            return self.heightOfTree(tree.root)
        else:
            print("N/A")
            return False

    def preorderPrint(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorderPrint(start.left, traversal)
            traversal = self.preorderPrint(start.right, traversal)
        return traversal

    def inorderPrint(self, start, traversal):
        if start:
            traversal = self.inorderPrint(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorderPrint(start.right, traversal)
        return traversal

    def postorderPrint(self, start, traversal):
        if start:
            traversal = self.postorderPrint(start.left, traversal)
            traversal = self.postorderPrint(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorderPrint(self, start):
        if start is None:
            return
        theQ = Queue()
        theQ.enqueue(start)
        traversal = ""

        while len(theQ)>0:
            traversal += (str(theQ.peek()) + "-")
            node = theQ.dequeue()
            
            if node.left:
                theQ.enqueue(node.left)
            if node.right:
                theQ.enqueue(node.right)

        return traversal

    def reverseorderPrint(self, start):
        if start is None:
            return
        from stack import stack
        theS = stack()
        theQ = Queue()
        theQ.enqueue(start)
        traversal = ""

        while len(theQ)>0:
            node = theQ.dequeue()
            theS.push(node)
            if node.right:
                theQ.enqueue(node.right)
            if node.left:
                theQ.enqueue(node.left)
        while not theS.is_empty():
            node = theS.pop()
            traversal += (str(node.value) + "-")
        return traversal

    def heightOfTree(self, node):
        if node is None:
            return -1
        leftNode = self.heightOfTree(node.left)
        rightNode = self.heightOfTree(node.right)
        return 1 + max(leftNode, rightNode)

    def sizeOfTree(self):
        if self.root is None:
            return 0
        from stack import stack
        theS = stack()
        theS.push(self.root)
        count = 1
        while theS:
            node = theS.pop()
            if node.left:
                count += 1
                theS.push(node.left)
            if node.right:
                count += 1
                theS.push(node.right)
        return count

    def sizeOfTreeRec(self, node):
        if node is None:
            return 0
        return 1 + self.sizeOfTreeRec(node.left) + self.sizeOfTreeRec(node.right)

tree = binaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
# tree.root.right.right.right = Node(8)

print(tree.helperPrint("preorder"))
print(tree.helperPrint("inorder"))
print(tree.helperPrint("postorder"))
print(tree.helperPrint("levelorder"))
print(tree.helperPrint("reverseorder"))
print(tree.helperPrint("heightoftree"))
print(tree.sizeOfTree())
print(tree.sizeOfTreeRec(tree.root))