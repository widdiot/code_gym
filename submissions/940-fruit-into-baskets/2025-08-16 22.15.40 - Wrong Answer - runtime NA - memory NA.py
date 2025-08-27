class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        hmap = defaultdict(int)
        hset = set()
        res = 0
        for j in range(len(fruits)):
            while len(hset) > 2:
                hmap[fruits[i]] = 0
                if fruits[i] in hset:
                    hset.remove(fruits[i])
                i += 1
            hmap[fruits[j]] += 1
            hset.add(fruits[j])
            if len(hset) <= 2:
                num_fruits = 0
                for f in hset:
                    num_fruits += hmap[f]
                if num_fruits > res:
                    res = num_fruits
        return res