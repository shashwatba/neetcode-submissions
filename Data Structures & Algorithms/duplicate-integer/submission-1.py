class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateChecker = {}
        for num in nums:
            if num not in duplicateChecker:
                duplicateChecker[num] = num
            else:
                return True
        return False