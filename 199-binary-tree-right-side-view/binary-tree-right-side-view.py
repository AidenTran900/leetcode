# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:

        view = []

        def solve(cur, layer):
            if not cur:
                return

            if layer >= len(view):
                view.append(cur.val)
            else:
                view[layer] = cur.val

            if cur.left:
                solve(cur.left, layer + 1)

            if cur.right:
                solve(cur.right, layer + 1)

        solve(root, 0)

        return view