class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq

        self.answer = []
        self.k = k
        for num in nums:
            self.answer.append(num)
        heapq.heapify(self.answer)

        i = len(nums)

        while i > k:
            heapq.heappop(self.answer)
            i -= 1
        

    def add(self, val: int) -> int:
        if len(self.answer) < self.k:
            heapq.heappush(self.answer,val)
        elif val >= self.answer[0]:
            heapq.heapreplace(self.answer, val)

        return self.answer[0]


        
