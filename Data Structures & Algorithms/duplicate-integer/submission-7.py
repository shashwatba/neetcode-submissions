class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapOfNums = {}
        for num in nums:
            if num in mapOfNums:
                return True
            mapOfNums[num] = num
        return False