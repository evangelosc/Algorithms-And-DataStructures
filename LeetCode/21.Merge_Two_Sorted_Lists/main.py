#!/usr/bin/python
from solution import *

# Unit Test

l1 = ListNode([1,2,3])
l2 = ListNode([1,2,3,4,5])

l11 = ListNode([])
l22 = ListNode([])

l111 = ListNode([])
l222 = ListNode([0])

solutionObject1 = Solution()
solutionObject2 = Solution()
solutionObject3 = Solution()
print(solutionObject1.mergeTwoLists(l1,l2).val)
print(solutionObject2.mergeTwoLists(l11, l22).val)
print(solutionObject3.mergeTwoLists(l111, l222).val)
