from collections import defaultdict
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i, j = 0, k
        hmap = defaultdict(int)
        for idx in range(i, min(len(nums), j+1)):
            if hmap[nums[idx]]:
                return True
            else:
                hmap[nums[idx]] += 1
        
        j += 1   
        while j < len(nums):
            print(hmap)
            hmap[nums[i]] -= 1
            i += 1
            if hmap[nums[j]]:
                return True
            else:
                hmap[nums[j]] += 1
            j += 1
        return False

         

