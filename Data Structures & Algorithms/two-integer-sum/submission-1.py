class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            pointer = nums[i]
            for j in range(len(nums)):
                if j == i:
                    j+=1
                if nums[j] + pointer == target:
                    return [i,j]