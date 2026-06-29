class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = nums1[0:m]
        b = nums2[0:n]
        counter = 0

        amountInA = m
        amountInB = n

        trackerA, trackerB = 0, 0

        while amountInA != 0 and amountInB != 0:
            if a[trackerA] < b[trackerB]:
                nums1[counter] = a[trackerA]
                counter += 1
                trackerA += 1
                amountInA -= 1
            else:
                nums1[counter] = b[trackerB]
                counter += 1
                trackerB += 1
                amountInB -= 1
            print(nums1)



        while amountInA != 0:
            nums1[counter] = a[trackerA]
            trackerA += 1
            amountInA -= 1
            counter += 1

        while amountInB != 0:
            nums1[counter] = b[trackerB]
            trackerB += 1
            amountInB -= 1
            counter += 1
        

        