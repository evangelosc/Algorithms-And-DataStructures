class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Basic BST functions
class binarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, curNode):
        if data < curNode.data:
            if curNode.left is None:
                curNode.left = Node(data)
            else:
                return self._insert(data, curNode.left)
        elif data > curNode.data:
            if curNode.right is None:
                curNode.right = Node(data)
            else:
                return self._insert(data, curNode.right)
        else:
            print("We cannot allow dublicates") 

    def find(self, data):
        if self.root:
            found = self._find(data, self.root)
            if found:
                return True
            return False
        return False

    def _find(self, data, curNode):
        if data < curNode.data and curNode.left:
            return self._find(data, curNode.left)
        elif data > curNode.data and curNode.right:
            return self._find(data, curNode.right)
        if data == curNode.data:
            return True        

    def inorderPrint(self, start, traversal):
        if start:
            traversal = self.inorderPrint(start.left, traversal)
            traversal += (str(start.data) + "-")
            traversal = self.inorderPrint(start.right, traversal)  
        return traversal
    
    def hPrint(self, key):
        if key == "BST":
            print(self.inorderPrint(theTree.root, ""))
        elif key == "NA":
            print(self.inorderPrint(theTreeF.root, ""))
        else:
            pass

    def isBST(self):
        if self.root:
            isSatisfied = self._isBST(self.root, self.root.data)
            if isSatisfied is None:
                return True
            return False
        return True
    
    def _isBST(self, curNode, data):
        if curNode.left:
            if data > curNode.left.data:
                return self._isBST(curNode.left, curNode.left.data)
            else:
                return False
        if curNode.right:
            if data < curNode.right.data:
                return self._isBST(curNode.right, curNode.right.data)
            else:
                return False



theTree = binarySearchTree()
theTree.insert(4)
theTree.insert(2)
theTree.insert(8)
theTree.insert(5)
theTree.insert(10)
theTree.insert(10)

theTreeF = binarySearchTree()
theTreeF.root = Node(1)
theTreeF.root.left = Node(2)
theTreeF.root.right = Node(3) 

print(theTree.find(10))
theTree.hPrint("BST")
theTreeF.hPrint("NA")
print(theTreeF.isBST())
print(theTree.isBST())
