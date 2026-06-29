class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = {}
        for i in range(0, len(nums)):
            if nums[i] in answer:
                return [answer[nums[i]], i]
            answer[target-nums[i]] = i
        