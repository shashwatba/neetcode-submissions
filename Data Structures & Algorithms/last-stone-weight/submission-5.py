class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            a = heapq.heappop_max(stones)
            b = heapq.heappop_max(stones)
            
            if a == b:
                continue
            y = abs(a - b)
            heapq.heappush_max(stones, y)

        if len(stones) == 1:
            return stones[0]
        return 0
        