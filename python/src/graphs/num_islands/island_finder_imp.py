from collections import deque
from dataclasses import dataclass
from typing import List, Optional

from src.graphs.num_islands.island_finder import IslandFinder


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    value: str


class IslandFinderImp(IslandFinder):

    def __init__(self):
        self.visited: set[Point] = set()
        self.width: int = 0
        self.height: int = 0
        self.grid: List[List[str]] = []

    def get_islands_number(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.width, self.height = self.get_dimensions()
        island_nums = 0

        for row in range(self.height):
            for col in range(self.width):
                node = Point(x=col, y=row, value=grid[row][col])
                if node.value == "1" and node not in self.visited:
                    self.explore_island(node)
                    island_nums += 1
        return island_nums

    def get_dimensions(self) -> tuple[int, int]:
        return len(self.grid[0]), len(self.grid)

    def explore_island(self, point: Point):
        queue: deque[Point] = deque()
        queue.append(point)

        while queue:
            point = queue.popleft()
            self.visited.add(point)

            neighbors = self.get_neighbors(point)
            for neighbor in neighbors:
                if neighbor not in self.visited:
                    queue.append(neighbor)

    def get_neighbors(self, point: Point) -> List[Point]:
        top_neighbor = self.get_neighbor_from_xy(point.x, point.y + 1)
        bottom_neighbor = self.get_neighbor_from_xy(point.x, point.y - 1)
        left_neighbor = self.get_neighbor_from_xy(point.x - 1, point.y)
        right_neighbor = self.get_neighbor_from_xy(point.x + 1, point.y)
        return [neighbor for neighbor in [top_neighbor, bottom_neighbor, left_neighbor, right_neighbor] if
                neighbor is not None]

    def get_neighbor_from_xy(self, x: int, y: int) -> Optional[Point]:
        if 0 <= x < self.width and 0 <= y < self.height and self.grid[y][x] == "1":
            return Point(x=x, y=y, value=self.grid[y][x])
        return None
