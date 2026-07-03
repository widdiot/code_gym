class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge = {}
        stack = []
        res = [-1]*len(nums1)
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                nge[nums2[stack[-1]]] = nums2[i]
                stack.pop() 
            stack.append(i)
        print(nge)
        for i in range(len(nums1)):
            res[i] = nge.get(nums1[i], -1)
        return res