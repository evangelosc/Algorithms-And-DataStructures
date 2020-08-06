# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# LeetCode Easy

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return
        prev = None
        cur = head
        while cur.next:
            prev = cur
            cur = cur.next
            if cur.val == prev.val:
                prev.next = cur.next
                cur = prev
        return head