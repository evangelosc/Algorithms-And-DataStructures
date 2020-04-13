class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#insertion, deletion and swapping!
class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        curNode = self.head
        while curNode:
            print(curNode.data)
            curNode = curNode.next

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        
        lastNode = self.head
        while lastNode.next:
            lastNode = lastNode.next
        lastNode.next = newNode

    def prepend(self, data):
        newNode = Node(data)

        newNode.next = self.head
        self.head = newNode

    def insertAfterNode(self, previousNode, data):
        if not previousNode:
            return
        newNode = Node(data)
        newNode.next = previousNode.next
        previousNode.next = newNode


    def deletion(self, key):
        curNode = self.head
        if curNode and curNode.data == key:
            self.head = curNode.next
            curNode = None
            return

        prev = None
        while curNode and curNode.data != key:
            prev = curNode
            curNode = curNode.next
        if curNode is None:
            return

        prev.next = curNode.next
        curNode = None

    def posDeletion(self, pos):
        curNode = self.head
        if pos == 0:
            self.head = curNode.next
            curNode = None
            return
        prev = None
        count = 0
        while curNode and count!=pos:
            count+=1
            prev = curNode
            curNode = curNode.next

        if curNode is None:
            return
        
        prev.next = curNode.next
        curNode = None

    def lengthList(self):
        curNode = self.head
        count = 0
        while curNode:
            count+=1
            curNode = curNode.next
        return count
        
    def lengthRecursive(self, node):
        if node is None:
            return 0
        return 1 + self.lengthRecursive(node.next)

    def swapNodes(self, key1, key2):
        if key1 == key2:
            return

        prev1 = None
        cur1 = self.head
        while cur1 and cur1.data != key1:
            prev1 = cur1
            cur1 = cur1.next
        prev2 = None
        cur2 = self.head
        while cur2 and cur2.data != key2:
            prev2 = cur2
            cur2 = cur2.next

        if not cur1 and not cur2:
            return
        if prev1:
            prev1.next = cur2
        else:
            self.head = cur2
        if prev2:
            prev2.next = cur1
        else:
            self.head = cur1

        cur1.next, cur2.next = cur2.next, cur1.next

    def reverseList(self):
        prev = None
        cur = self.head
        while cur:
            tempNxt = cur.next
            cur.next = prev
            prev = cur
            cur = tempNxt
        self.head = prev

    def reverseListRec(self):
        def reverseHelper(cur, prev):
            if not cur:
                return prev
            tempNxt = cur.next
            cur.next = prev
            prev = cur
            cur = tempNxt
            return reverseHelper(cur=cur, prev=prev)
        self.head = reverseHelper(cur=self.head, prev=None)

    def mergeList(self, llist):
        p = self.head
        q = llist.head
        s = None

        if p is None:
            return q
        if q is None:
            return p

        if p.data <= q.data:
            s = p
            p = s.next
        else:
            s = q
            q = s.next
        newHead = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if p is None:
            s.next = q
        else:
            s.next = p
        return newHead

    def removeDublicates(self):
        prev = None
        cur = self.head

        removeDoubles = dict()
        while cur:
            if cur.data in removeDoubles:
                prev.next = cur.next
                cur = None
            else:
                removeDoubles[cur.data] = 1
                prev = cur
            cur = prev.next

    def theNthToTheLastNode(self, num):
        count = 1
        cur = self.head
        while cur:
            if count == num:
                return cur.data
            else:
                count += 1
                cur = cur.next
            
    def numberOfOccurrences(self):
        cur = self.head
        numbersO = dict()
        while cur:
            if cur.data in numbersO:
                numbersO[cur.data] += 1
            else:
                numbersO[cur.data] = 1
            cur = cur.next
        return numbersO

    def numberOfOccurrencesRec(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.numberOfOccurrencesRec(node.next, data)
        else:
            return self.numberOfOccurrencesRec(node.next, data)

    def rotateALList(self, num):
        p = self.head
        q = self.head
        prev = None
        count = 1
        while p and count < num:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev

        while q:
            prev = q
            q = q.next
        q = prev

        q.next = self.head
        self.head = p.next
        p.next = None

    def palindrome(self):
        # Method 1
        p = self.head
        ourStr = ""
        while p:
            ourStr += p.data
            p = p.next
        return ourStr == ourStr[::-1]

        # Method 2
        # p = self.head
        # ourData = list()
        # while p:
        #     ourData.append(p.data)
        #     p = p.next
        # p = self.head
        # while p:
        #     if ourData.pop() != p.data:
        #         return False
        #     p = p.next
        # return True

    def moveTailToHead(self):
        cur = self.head
        prev = None
        while cur.next:
            prev = cur
            cur = prev.next

        cur.next = self.head
        self.head = cur
        prev.next = None

    def sumTwoList(self, llist):
        p = self.head
        q = llist.head
        carry = 0
        theList = LinkedList()
        while p and q:
            data = p.data + q.data
            data += carry
            if data//10 > 0:
                carry = data//10
            theList.append(data%10)
            p = p.next
            q = q.next

        theList.print()

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
            


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("E1")
llist.insertAfterNode(llist.head.next.next, "E2")
llist.print()
print("=============")
llist.deletion("E1")
llist.deletion("E2")
llist.print()
print("=============")
llist.posDeletion(2)
llist.print()
print('=============')
llist.insertAfterNode(llist.head.next, "C")
llist.append("E")
llist.append("F")
llist.print()
print('=============')
print(llist.lengthList())
ll = llist.lengthRecursive(llist.head)
print(ll)
print('=============')
llist.swapNodes("A", "B")
llist.swapNodes("B", "C")
llist.print()
print('=============')
llist.swapNodes("B", "C")
llist.swapNodes("A", "B")
llist.print()
print('=============')
llist.reverseList()
llist.print()
print('=============')
llist.reverseListRec()
llist.print()
print('=============')
llist1 = LinkedList()
llist1.append(1)
llist1.append(5)
llist1.append(7)
llist1.append(9)
llist1.append(10)
llist1.print()
print('=============')
llist2 = LinkedList()
llist2.append(2)
llist2.append(3)
llist2.append(4)
llist2.append(6)
llist2.append(8)
llist2.print()
print('=============')
llist1.mergeList(llist2)
llist1.print()
print('=============')
llistDual = LinkedList()
llistDual.append(1)
llistDual.append(2)
llistDual.append(3)
llistDual.append(2)
llistDual.append(2)
llistDual.append(4)
llistDual.append(6)
llistDual.append(2)
llistDual.append(2)
llistDual.append(3)
llistDual.append(1)
llistDual.print()
theNumber = llistDual.numberOfOccurrences()
theNumber2 = llistDual.numberOfOccurrencesRec(llistDual.head, 2)
print(theNumber)
print(theNumber2)
print('=============')
llistDual.removeDublicates()
llistDual.print()
print('=============')
llista = LinkedList()
llista.append("A")
llista.append("B")
llista.append("C")
llista.append("D")
theNthNode = llista.theNthToTheLastNode(2)
print(theNthNode)
print('=============')
llistDual.insertAfterNode(llistDual.head.next.next.next, 5)
llistDual.print()
print('=============')
llistDual.rotateALList(5)
llistDual.print()
print('=============')
llistnp = LinkedList()
llistnp.append("A")
llistnp.append("B")
llistnp.append("C")
llistnp.append("D")
print(llistnp.palindrome())
print('=============')
llistp = LinkedList()
llistp.append("R")
llistp.append("A")
llistp.append("D")
llistp.append("A")
llistp.append("R")
print(llistp.palindrome())
print('=============')
llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.moveTailToHead()
llist.print()
print('=============')
llist = LinkedList()
llist.append(5)
llist.append(6)
llist.append(3)
llistt = LinkedList()
llistt.append(8)
llistt.append(4)
llistt.append(0)
llist.sumTwoList(llistt)

