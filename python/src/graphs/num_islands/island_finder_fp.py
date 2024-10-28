from collections import deque
from dataclasses import dataclass
from functools import reduce
from typing import List, Optional

from src.graphs.num_islands.island_finder import IslandFinder


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    value: str


class IslandFinderFP(IslandFinder):

    def get_islands_number(self, grid: List[List[str]]) -> int:
        width, height = len(grid[0]), len(grid)

        def get_neighbors(point: Point) -> List[Point]:
            offsets = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            neighbors = [get_neighbor_from_xy(point.x + offset[0], point.y + offset[1]) for offset in offsets]
            return [neighbor for neighbor in neighbors if neighbor is not None]

        def get_neighbor_from_xy(x: int, y: int) -> Optional[Point]:
            if 0 <= x < width and 0 <= y < height and grid[y][x] == "1":
                return Point(x=x, y=y, value=grid[y][x])
            return None

        def explore_island(point: Point, visited: set[Point]) -> set[Point]:
            def visit_neighbors(neighbors: deque[Point], _visited: set[Point]) -> set[Point]:
                if not neighbors:
                    return _visited
                curr_point = neighbors.popleft()
                new_visited = _visited | {curr_point}

                all_neighbors = get_neighbors(curr_point)
                all_neighbors_not_visited = deque([n for n in all_neighbors if n not in _visited])
                return visit_neighbors(neighbors + all_neighbors_not_visited, new_visited)

            return visit_neighbors(deque([point]), visited)

        def sum_all_islands(acc: tuple[int, set[Point]], point: Point) -> tuple[int, set[Point]]:
            num_islands, visited = acc
            if point not in visited and point.value == "1":
                new_visited = explore_island(point, visited)
                return num_islands + 1, new_visited
            return num_islands, visited

        coordinates = [Point(x=col, y=row, value=grid[row][col]) for col in range(width) for row in range(height)]
        num_islands, visited = reduce(sum_all_islands, coordinates, (0, set()))
        return num_islands
