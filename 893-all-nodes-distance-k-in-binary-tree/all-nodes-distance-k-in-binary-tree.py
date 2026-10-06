# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 1 turn into adjacency list -> O(n) time, O(n) space
        # 2 do a DFS starting at target -> O(n) time
        # Time: O(n)
        # Space: O(n)
        
        # 1
        adj_list = {}
        
        def create_adj(cur, parent_val):
            if not cur:
                return

            val = cur.val
            adj_list[val] = []

            # reminder that 0 = False, so use "is not None"
            if parent_val is not None:
                adj_list[val].append(parent_val)

            if cur.left:
                adj_list[val].append(cur.left.val)

            if cur.right:
                adj_list[val].append(cur.right.val)

            create_adj(cur.left, val)
            create_adj(cur.right, val)
        
        create_adj(root, None)


        # 2
        result = []
        visited = set()

        print(adj_list)
        
        def get_dist_k(cur, dist):
            if dist == k:
                result.append(cur)
                return

            visited.add(cur)

            for adj in adj_list[cur]:
                if adj in visited: continue

                get_dist_k(adj, dist + 1)


        get_dist_k(target.val, 0)

        return result