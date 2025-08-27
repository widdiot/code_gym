def traverse(arr):
    maxProd = -10**5
    prod = 1
    for i in arr:
        prod *= i
        maxProd = max(maxProd, prod)
        if i == 0:
            prod = 1
    return maxProd

def findMaxProd(arr):
    frontMax = traverse(arr)
    backMax = traverse(arr[::-1])
    return max(frontMax, backMax)

class Solution:
    def maxProduct(self, nums: List[int]) -> int: 
        return findMaxProd(nums)
        