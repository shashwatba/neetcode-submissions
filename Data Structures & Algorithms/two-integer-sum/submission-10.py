class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_of_nums = {}
        for index, num in enumerate(nums):
            if target - num in map_of_nums:
                return [map_of_nums[target-num], index]
            else:
                map_of_nums[num] = index
