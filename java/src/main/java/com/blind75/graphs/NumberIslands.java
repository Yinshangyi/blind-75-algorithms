package com.blind75.graphs;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

record Position(int row, int col) {
};

public class NumberIslands {

    private char[][] gridIslands;
    private Set<Position> visited;

    public int numIslands(char[][] grid) {
        var numIslands = 0;
        gridIslands = grid;
        visited = new HashSet<>();

        for (int row = 0; row < grid.length; row++) {
            for (int col = 0; col < grid[row].length; col++) {
                var position = new Position(row, col);
                if (grid[row][col] == '1' && !visited.contains(position)) {
                    breadthFirstSearchIsland(position);
                    numIslands++;
                }
            }
        }
        return numIslands;
    }

    private void breadthFirstSearchIsland(Position position) {
        var queue = new ArrayList<Position>();
        queue.add(position);
        while (!queue.isEmpty()) {
            var currentPosition = queue.remove(0);
            visited.add(currentPosition);
            var newPositions = getNextPositions(currentPosition);
            for (var nextPosition : newPositions) {
                var validPosition = isPositionValid(nextPosition);
                if (validPosition) {
                    queue.add(nextPosition);
                    visited.add(nextPosition);
                }
            }
        }
    }

    private boolean isPositionValid(Position position) {
        return position.row() >= 0 && position.row() < gridIslands.length &&
                position.col() >= 0 && position.col() < gridIslands[0].length &&
                gridIslands[position.row()][position.col()] == '1' &&
                !visited.contains(position);
    }

    private List<Position> getNextPositions(Position position) {
        return List.of(
                new Position(position.row() - 1, position.col()), // UP
                new Position(position.row() + 1, position.col()), // DOWN
                new Position(position.row(), position.col() + 1), // RIGHT
                new Position(position.row(), position.col() - 1)  // LEFT
        );
    }
}
