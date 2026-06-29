class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for index in range(len(nums)):
            if nums[index] != val:
                nums[i] = nums[index]
                i += 1

        return i