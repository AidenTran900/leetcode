from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        # BFS flood fill O(1 * n)

        m = len(grid)
        n = len(grid[0])

        DIRS = [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]
        queue = deque()
        fresh_count = 0

        for y, row in enumerate(grid):
            for x, val in enumerate(row):
                if val == 1:
                    fresh_count += 1
                elif val == 2:
                    queue.append((x, y))

        if fresh_count == 0:
            return 0

        time = 0
        while queue:
            time += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()

                for direction in DIRS:
                    dx, dy = direction
                    new_x, new_y = x + dx, y + dy

                    if new_x >= n or new_x < 0 or new_y >= m or new_y < 0:
                        continue

                    if grid[new_y][new_x] == 1:
                        fresh_count -= 1
                        grid[new_y][new_x] = 2
                        queue.append((new_x, new_y))


        return (time - 1 if fresh_count == 0 else -1)