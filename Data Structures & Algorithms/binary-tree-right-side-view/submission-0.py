# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque

        node_tracker = deque()
        answer = []

        if root:
            node_tracker.append(root)

        while len(node_tracker) > 0:
            right_node = node_tracker.pop()
            answer.append(right_node.val)
            node_tracker.append(right_node)
            for i in range(len(node_tracker)):
                current_node = node_tracker.popleft()

                if current_node.left:
                    node_tracker.append(current_node.left)
                if current_node.right:
                    node_tracker.append(current_node.right)

        return answer
        