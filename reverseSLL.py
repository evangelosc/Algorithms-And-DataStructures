# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        prev = None
        cur = head
        for _ in range(1,m):
            prev = cur
            cur = cur.next
        
        h1 = cur
        cur2 = cur.next
        
        for _ in range(n-m):
            temp = cur2.next
            cur2.next = cur
            cur = cur2
            cur2 = temp
            
        if prev:
            prev.next = cur
        h1.next = cur2
        
        if m!= 1:
            return head
        return cur