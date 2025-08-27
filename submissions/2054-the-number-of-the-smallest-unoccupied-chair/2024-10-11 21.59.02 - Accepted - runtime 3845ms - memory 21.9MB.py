class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        sorted_idx = sorted(range(len(times)), key=lambda x: times[x][0])
        total_time = max([i for _, i in times])
        chair_times = [0] * len(times)
        for j in sorted_idx:
            arrival, departure = times[j]
            for i in range(len(chair_times)):
                if arrival >= chair_times[i]:
                    if j == targetFriend:
                        return i
                    chair_times[i] = departure
                    break
        return 0                
