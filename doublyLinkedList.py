class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        newNode = Node(data)
        if self.head is None:
            newNode.next = None
            newNode.prev = None
            self.head = newNode
        else:
            newNode.prev = None
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            newNode.prev = None
            newNode.next = None
            self.head = newNode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            newNode.prev = cur
            cur.next = newNode
            newNode.next = None

    def print(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    
    def buildNode(self, data):
        return Node(data)

    def addAfterNode(self, node, data):
        cur = self.head
        newNode = Node(data)
        if cur == node:
            cur.next = newNode
            newNode.prev = cur
            newNode.next = None
        else:
            while cur:
                cur = cur.next
                if cur == node:
                    tempNxt = cur.next
                    cur.next = newNode
                    newNode.prev = cur
                    newNode.next = tempNxt
                    tempNxt.prev = newNode

    def addBeforeNode(self, node, data):
        newNode = Node(data)
        cur = self.head
        if cur == node:
            cur.prev = newNode
            newNode.next = cur
            newNode.prev = None
            self.head = newNode
        else:
            preV = None
            while cur.next:
                preV = cur
                cur = cur.next
                if cur == node:
                    preV.next = newNode
                    newNode.prev = preV
                    newNode.next = cur
                    cur.prev = newNode

    def deleteNode(self, key):
        cur = self.head
        preV = None
        while cur:
            if cur.data == key and cur == self.head:
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                else:
                    tempNxt = cur.next
                    cur.next = None
                    tempNxt.prev = None
                    self.head = tempNxt
                    return
            elif cur.data == key:
                if cur.next:
                    preV.next = cur.next
                    cur.next.prev = preV
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                else:
                    preV.next = None
                    cur.prev = None
                    cur = None
                    return
            else:
                preV = cur
                cur = cur.next

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev
    
    def removeDublicates(self):
        cur = self.head
        # prev = None
        numberD = dict()
        while cur:
            if cur.data in numberD:
                nxt = cur.next
                self.deleteNode(cur.data)
                cur = nxt
            else:
                numberD[cur.data] = 1
                cur = cur.next

    def pairsWithSum(self, sumVal):
        p = self.head
        q = None
        pairs = list()
        while p:
            q = p.next
            while q:
                if p.data+q.data == sumVal:
                    pairs.append("("+str(p.data)+","+str(q.data)+")")
                q = q.next
            p = p.next
        return pairs
            


dLlist = doublyLinkedList()
dLlist.append(1)
dLlist.append(2)
dLlist.append(3)
dLlist.append(4)
dLlist.append(5)
dLlist.print()
print("+++++++++++++++++")
# dLlist.prepend(2)
# dLlist.print()
# print("+++++++++++++++++")
# dLlist.addAfterNode(dLlist.head.next, 2)
dLlist.print()
print("+++++++++++++++++")
dLlist.addBeforeNode(dLlist.head.next, 3433)
dLlist.print()
print("+++++++++++++++++")
dLlist.deleteNode(3433)
dLlist.print()
# print("+++++++++++++++++")
# dLlist.reverse()
# dLlist.print()
print("+++++++++++++++++")
dLlist.append(2)
dLlist.append(1)
dLlist.append(3)
dLlist.append(3)
dLlist.append(2)
dLlist.removeDublicates()
dLlist.print()
dLlist.append(4)
dLlist.append(8)
dLlist.append(7)
print(dLlist.pairsWithSum(111))