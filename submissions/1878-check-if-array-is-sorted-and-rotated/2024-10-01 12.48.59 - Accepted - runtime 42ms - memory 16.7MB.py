class Solution:
    def is_sorted(self, arr, start, end):
        for j in range(start, end):
            j1 = j
            j2 = j + 1
            if j1 > len(arr) - 1:
                j1 = j1 - len(arr)
            if j2 > len(arr) - 1:
                j2 = j2 - len(arr)
            print(f"{j1}, {j2}")
            if arr[j2] < arr[j1]:
                return False
        return True

    def check(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)):
            if self.is_sorted(nums, i,i+len(nums)-1):
                return True
        return False

        