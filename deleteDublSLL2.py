# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        save_head = ListNode(0)
        save_head.next = head
        prev = save_head
        foundDuplicates = False
        
        while head and head.next:
            while head and head.next and head.val == head.next.val:
                foundDuplicates = True
                head = head.next
            if foundDuplicates:
                prev.next = head.next
                foundDuplicates = False
            else:
                prev = head
            head = head.next
            
        return save_head.next