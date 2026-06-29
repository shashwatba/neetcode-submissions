class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_checker = {}

        for num in nums:
            if num in duplicate_checker:
                return True
            duplicate_checker[num] = 1

        return False
