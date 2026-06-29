class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k <= largest value, k >= smallest value
        # add up all values, then divide by k, must be <= h
        # k is a value in piles
        # search from range of smallest to largest value


        tracker = 0
        left, right = 1, max(piles)
        while left <= right:
            middle = (left + right) // 2
            hours = 0
            for p in piles:
                hours += (p + middle - 1) // middle
            if hours <= h:
                tracker = middle
                right = middle - 1
            else:
                left = middle + 1
        
        return tracker
