from collections import deque
from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        def breadthFirstSearch(row: int, col: int):
            queue = deque()
            visited.add((row, col))
            queue.append((row, col))
            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for offsetX, offsetY in directions:
                    newRow = row + offsetX
                    newCol = col + offsetY
                    if (newRow in range(rows)
                            and newCol in range(cols)
                            and grid[newRow][newCol] == "1"
                            and (newRow, newCol) not in visited):
                        queue.append((newRow, newCol))
                        visited.add((newRow, newCol))

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islandCount = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    breadthFirstSearch(row, col)
                    islandCount += 1
        return islandCount
