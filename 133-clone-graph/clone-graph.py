"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}

        # 1 clone all nodes, map to old
        visited = set()
        def clone_nodes(cur):
            if cur in visited:
                return
            visited.add(cur)
            old_to_new[cur] = Node(cur.val)

            for neighbor in cur.neighbors:
                clone_nodes(neighbor)

        clone_nodes(node)

        # 2 connect cloned nodes
        visited = set()
        def connect_clones(cur):
            if cur in visited:
                return

            visited.add(cur)
            for neighbor in cur.neighbors:
                old_to_new[cur].neighbors.append(old_to_new[neighbor])
                connect_clones(neighbor)
        
        connect_clones(node)

        return old_to_new[node]