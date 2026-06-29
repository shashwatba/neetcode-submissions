# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_list = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            print(root.val)
            inorder_list.append(root.val)
            print(inorder_list)
            dfs(root.right)

        dfs(root)
        return inorder_list
        