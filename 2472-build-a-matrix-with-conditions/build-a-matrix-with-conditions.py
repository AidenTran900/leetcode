class Solution:

    def createAdj(self, k: int, conditions: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(k + 1)]

        for u, v in conditions:
            adj[u].append(v)

        return adj

    def topoSort(self, k : int, adj : List[List[int]]) -> List[int]:
        indegree = [0] * (k + 1)

        # Compute indegrees
        for i in range(1, k + 1):
            for neighbor in adj[i]:
                indegree[neighbor] += 1
                
        queue = deque([i for i in range(1, k + 1) if indegree[i] == 0])
        res = []

        # Kahn’s Algorithm
        while queue:
            node = queue.popleft()
            res.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return res if len(res) == k else []
            
        

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        # Convert conditions -> adjacency map
        row_adj = self.createAdj(k, rowConditions)
        col_adj = self.createAdj(k, colConditions)

        # Topological sort
        row_sort = self.topoSort(k, row_adj)
        col_sort = self.topoSort(k, col_adj)

        if not row_sort or not col_sort:
            return []

        # Combine to matrix
        row_pos = {row_sort[i]: i for i in range(len(row_sort))}
        col_pos = {col_sort[i]: i for i in range(len(col_sort))}

        matrix = [[0] * k for _ in range(k)]
        for val in range(1, k + 1):
            r = row_pos[val]
            c = col_pos[val]
            matrix[r][c] = val

        return matrix
                
        




        

        


        