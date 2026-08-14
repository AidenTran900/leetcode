from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def traverse(pItem, qItem):
            if pItem == None and qItem != None:
                return False

            if qItem == None and pItem != None:
                return False

            if qItem == None and pItem == None:
                return True

            if pItem.val != qItem.val:
                return False

            return traverse(pItem.left, qItem.left) and traverse(pItem.right, qItem.right)

        return traverse(p, q)  




