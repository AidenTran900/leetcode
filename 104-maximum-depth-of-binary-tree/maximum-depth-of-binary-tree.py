# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Use DFS since don't need to explore every node
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(root, depth):
            if root == None:
                return depth

            depth += 1
            left = helper(root.left, depth)
            right = helper(root.right, depth)

            return max(left, right)

        return helper(root, 0)
