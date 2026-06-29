class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        inner_size = len(matrix[0]) - 1


        while left <= right:
            middle = (left + right) // 2
            if matrix[middle][0] <= target and matrix[middle][inner_size] >= target:
                #binary search
                inner_left, inner_right = 0, inner_size
                while inner_left <= inner_right:
                    inner_middle = (inner_left + inner_right) // 2
                    if matrix[middle][inner_middle] > target:
                        inner_right = inner_middle - 1
                    elif matrix[middle][inner_middle] < target:
                        inner_left = inner_middle + 1
                    else:
                        return True
                return False


            elif matrix[middle][0] > target:
                right = middle - 1
            else:
                left = middle + 1


        return False
                