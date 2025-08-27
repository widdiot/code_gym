def traverse(arr):
    maxProd = -10**5
    prod = 1
    for i in arr:
        prod *= i
        maxProd = max(maxProd, prod)
    return maxProd

def findMaxProd(arr):
    frontMax = traverse(arr)
    backMax = traverse(arr[::-1])
    return max(frontMax, backMax)

class Solution:
    def maxProduct(self, nums: List[int]) -> int: 
        arrs = []
        arr = []
        for i in nums:
            if i != 0:
                arr.append(i)
            else:
                arrs.append(arr)
                arrs.append([0])
                arr = []
        arrs.append(arr)
        print(arrs)
        max_list = [findMaxProd(arr) for arr in arrs]
        return max(max_list)
        