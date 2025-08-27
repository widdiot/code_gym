class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        i, j = 0 , len(people) - 1
        res = 0
        while i <= j:
            if people[j] >= limit:
                res += 1
                j -= 1
            elif people[j] + people[i] <= limit:
                res += 1
                j -= 1
                i += 1
            else:
                res += 1
                j -= 1
        return res