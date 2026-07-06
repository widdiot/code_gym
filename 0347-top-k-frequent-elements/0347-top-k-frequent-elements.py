import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        for n in nums:
            hmap[n] = hmap.get(n, 0) + 1
        nums = [(hmap[n], n) for n in hmap]
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return [n[1] for n in nums] 

