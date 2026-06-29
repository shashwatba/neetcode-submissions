class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in checker:
                return [checker[difference], index]
            else:
                checker[num] = index