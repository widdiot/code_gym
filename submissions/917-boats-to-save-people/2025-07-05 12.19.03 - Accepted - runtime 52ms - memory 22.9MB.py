class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        l, r = 0, len(people)-1
        num_boats = 0
        while l < r:
            if people[r] == limit or people[l] + people[r] > limit:
                num_boats += 1
                r -= 1
            elif people[l] + people[r] <= limit:
                num_boats += 1
                l += 1
                r -= 1
        if l == r:
            num_boats += 1
        return num_boats 