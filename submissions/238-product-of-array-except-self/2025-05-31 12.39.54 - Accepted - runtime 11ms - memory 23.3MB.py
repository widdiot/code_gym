class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod = 1
        num_zeros = 0
        for i in nums:
            if i != 0:
                prod *= i
            else:
                num_zeros += 1

        answer = []
        for i in nums:
            if i != 0:
                if num_zeros == 0:
                    answer.append(prod//i)
                else:
                    answer.append(0)
            else:
                if num_zeros == 1: 
                    answer.append(prod)
                elif num_zeros > 1:
                    answer.append(0)
        return answer