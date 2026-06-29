class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
            else:
                if max < current:
                    max = current
                current = 0
        
        if max < current:
            return current
        
        return max
        