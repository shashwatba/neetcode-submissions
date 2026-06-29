class Solution:
    import heapq
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapq.heapify_max(stones)
        print(stones)
        while len(stones) > 1:
            a = heapq.heappop_max(stones)
            b = heapq.heappop_max(stones)
            
            print(a, b)
            if a == b:
                print("in a==b")
                print(stones)
                continue
            y = abs(a - b)
            heapq.heappush_max(stones, y)
            print(stones)

        if len(stones) == 1:
            return stones[0]
        return 0
        