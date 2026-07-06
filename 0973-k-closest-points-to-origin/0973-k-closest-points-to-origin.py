# a max heap of the closest k points
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(-(p[0]**2 + p[1]**2)**(1/2), p) for p in points]
        heapq.heapify(points)
        while len(points) > k:
            heapq.heappop(points)
        return [t[1] for t in points]