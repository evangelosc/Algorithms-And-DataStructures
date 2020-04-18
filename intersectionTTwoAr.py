class Solution:
    def intersect(self, nums1, nums2):
        res = list()
        if len(nums1) > len(nums2):
            for el in nums2:
                if el in nums1:
                    res.append(el)
                    print(res, nums2)
                    nums1.remove(el)
            return res
        else:
            for el in nums1:
                if el in nums2:
                    res.append(el)
                    nums2.remove(el)
            return res

    def inter2(self, nums1, nums2):
        res = list()
        hashT = dict()
        for el in nums1:
            if el in hashT:
                hashT[el] += 1
            else:
                hashT[el] = 1
        for el in nums2:
            if el in hashT:
                hashT[el] = 'found'
            else:
                hashT[el] = 1
        for keys, values in hashT.items():
            if values == 'found':
                res.append(keys)
                # print(keys,values)
            print(keys,values)
        return res

sol = Solution()
print(sol.intersect([1,2,2,1],[2,2]))
# print(sol.inter2([1,2,2,1],[2,2]))