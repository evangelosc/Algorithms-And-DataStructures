# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1 and l2:
            return l2
        if l1 and not l2:
            return l1
        curNum = 0
        s = 0
        r = 0
        fake = ListNode(-1)
        res = fake
        while l1 or l2:
            s = 0
            curNum = 0
            curNum += r
            if l1:
                curNum += l1.val
            if l2:
                curNum += l2.val
            if curNum >= 10:
                r = curNum//10
                s = curNum%10
            else:
                r = 0
                s = curNum
            res.next = ListNode(s)
            res = res.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if r == 1:
            res.next = ListNode(1)
        return fake.next