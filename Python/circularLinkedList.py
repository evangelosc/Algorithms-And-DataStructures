class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLList:
    def __init__(self):
        self.head = None
    
    def _print(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def _append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.head.next = self.head
        else:
            lastNode = self.head
            while lastNode.next != self.head:
                lastNode = lastNode.next
            lastNode.next = newNode
            newNode.next = self.head

    def _prepend(self, data):
        newNode = Node(data)
        cur = self.head
        newNode.next = self.head
        if self.head is None:
            newNode.next = newNode
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
        self.head = newNode


    def _remove(self, key):
        cur = self.head
        if key == cur.data:
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.data != key:
                prev = cur
                cur = cur.next
            prev.next = cur.next
            cur = None

    def lengthCLList(self):
        cur = self.head
        count = 1
        while cur.next != self.head:
            count += 1
            cur = cur.next
        return count

    def _split(self):
        size = self.lengthCLList()
        if size == 0:
            return None
        if size == 1:
            return self.head
        mid = size/2
        countList = 1
        cur = self.head
        prev = None
        while countList <= mid:
            countList += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        newLList = CircularLList()
        while countList < size:
            countList += 1
            newLList._append(cur.data)
            cur = cur.next
        newLList._append(cur.data)
        self._print()
        print("\n")
        newLList._print()

    def _removeNode(self, node):
        cur = self.head
        if cur == node:
            count = 1
            while count != self.lengthCLList():
                count += 1
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next

    def _josephusProblem(self, step):
        cur = self.head
        while self.lengthCLList() > 1:
            count = 1
            while count != step:
                count += 1
                cur = cur.next
            self._removeNode(cur)
            cur = cur.next
    def isCircular(self):
        cur = self.head
        while (cur.next != self.head):
            cur = cur.next
            if not cur:
                break
        if cur is None:
            print('singly LinkedList')
        if cur is self.head:
            print('Circular LinkedList')

    

cllist = CircularLList()
cllist._append("A")
cllist._append("B")
cllist._append("C")
cllist._append("D")
cllist._prepend("E1")
cllist._print()
print("=============")
cllist._remove("E1")
cllist._print()
print("=============")
# cllist._split()
print("=============")
cllist._josephusProblem(3)
# cllist._removeNode(cllist.head.next.next.next)
cllist._print()
from singlyLinkedList import LinkedList
slist = LinkedList()
slist.append("A")
slist.append("B")
slist.append("C")
slist.append("D")
cllist.isCircular()
slist.isCircular()
