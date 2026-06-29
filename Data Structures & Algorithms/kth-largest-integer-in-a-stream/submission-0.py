class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.answer = []
        self.k = k
        for num in nums:
            self.answer.append(num)
        

    def add(self, val: int) -> int:

        self.answer.append(val)
        self.answer.sort()
        print(self.answer)

        i = len(self.answer) - self.k
        return self.answer[i]


        
