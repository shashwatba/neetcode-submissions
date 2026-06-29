# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        node_tracker = deque()
        answer = []

        if root:
            node_tracker.append(root)
        
        while len(node_tracker) > 0:
            current_level = []
            for i in range(len(node_tracker)):
                current_node = node_tracker.popleft()
                current_level.append(current_node.val)

                if current_node.left:
                    node_tracker.append(current_node.left)
                if current_node.right:
                    node_tracker.append(current_node.right)
            
            answer.append(current_level)

        return answer



        