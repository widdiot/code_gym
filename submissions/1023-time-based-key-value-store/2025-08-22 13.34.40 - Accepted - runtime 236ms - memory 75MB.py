from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list)

    def search_insert_idx(self, key, timestamp):
        if len(self.tmap[key]) == 0:
            return 0
        i, j = 0, len(self.tmap[key])-1
        res = len(self.tmap[key])
        while i <= j:
            mid = (i+j)//2
            if timestamp <= self.tmap[key][mid][1]:
                res = mid
                j = mid - 1
            else:
                i = mid + 1
        return res

    def lower_bound(self, key, timestamp):
        i, j = 0, len(self.tmap[key])-1
        res = -1
        while i <= j:
            mid = (i+j)//2
            if timestamp >= self.tmap[key][mid][1]:
                res = mid
                i = mid + 1
            else:
                j = mid - 1
        return res

    def set(self, key: str, value: str, timestamp: int) -> None:
        idx = self.search_insert_idx(key, timestamp)
        self.tmap[key].insert(idx, [value, timestamp])
    
    def get(self, key: str, timestamp: int) -> str:
        idx = self.lower_bound(key, timestamp)
        if idx >= 0:
            return self.tmap[key][idx][0]
        else:
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)