# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path = []
        answer = 0

        def traversal(root, targetSum, path, answer):
            if not root:
                return False

            answer += root.val
            path.append(root.val)
            if not root.left and not root.right:
                if answer == targetSum:
                    return True
            
            if traversal(root.left, targetSum, path, answer):
                return True
            
            if traversal(root.right, targetSum, path, answer):
                return True
            
            a = path.pop()
            answer -= a
            return False
        
        return traversal(root, targetSum, path, answer)
        