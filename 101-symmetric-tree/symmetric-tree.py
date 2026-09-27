# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root == None:
            return False
        
        def traverse(left, right) -> bool:
            if not left and not right:
                return True
            if not right or not left:
                return False
            
            is_equal = left.val == right.val
            traverse_left = traverse(left.left, right.right)
            traverse_right = traverse(right.left, left.right)

            return is_equal and traverse_left and traverse_right
            

        return traverse(root.left, root.right)
            