#!/usr/bin/python


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first = m - 1
        second = n - 1
        i = m + n - 1
        while(i>=0):
            if second < 0:
                break
            if (nums1[first]>nums2[second])and(first>=0):
                nums1[i] = nums1[first]
                first -= 1
            else:
                nums1[i] = nums2[second]
                second -= 1
            i -= 1
        return nums1