def display_forest(forest):
    for row in forest:
        print(" ".join(row))


def check_coordinates_valid(forest, row, col):
    # unvalid condition for the row
    if row < 0 or row > len(forest) - 1:
        return False
    # unvalid condition for the col
    if col < 0 or col > len(forest[0]) - 1:
        return False
    # unvalid condition for no tree
    if forest[row][col] == ".":
        return False
    return True


def find_neighbors(forest, tree_row, tree_col):
    valid_neighbors = []
    left_tree_coord = [tree_row, tree_col - 1]
    if check_coordinates_valid(forest, left_tree_coord[0], left_tree_coord[1]):
        valid_neighbors.append([left_tree_coord[0], left_tree_coord[1]])

    right_tree_coord = [tree_row, tree_col + 1]
    if check_coordinates_valid(forest, right_tree_coord[0], right_tree_coord[1]):
        valid_neighbors.append([right_tree_coord[0], right_tree_coord[1]])

    top_tree_coord = [tree_row - 1, tree_col]
    if check_coordinates_valid(forest, top_tree_coord[0], top_tree_coord[1]):
        valid_neighbors.append([top_tree_coord[0], top_tree_coord[1]])

    bottom_tree_coor = [tree_row + 1, tree_col]
    if check_coordinates_valid(forest, bottom_tree_coor[0], bottom_tree_coor[1]):
        valid_neighbors.append([bottom_tree_coor[0], bottom_tree_coor[1]])
    return valid_neighbors


def propagate_fire(forest, start_row, start_col):
    queue = []
    queue.append([start_row, start_col])
    while queue:
        tree_coord = queue.pop(0)
        row = tree_coord[0]
        col = tree_coord[1]

        point = [0, 1]


        forest[row][col] = "F"
        neighbors = find_neighbors(forest, row, col)
        for neighbor in neighbors:
            queue.append(neighbor)


forest = [
    [".", "T", ".", "T"],
    [".", "T", "T", "."],
    [".", "T", ".", "."],
    ["T", ".", ".", "."]
]

expected_forest = [
    [".", "F", ".", "T"],
    [".", "F", "F", "."],
    [".", "F", ".", "."],
    ["T", ".", ".", "."]
]
display_forest(forest)
propagate_fire(forest, 2, 1)
print()
display_forest(forest)
if forest == expected_forest:
    print("ok")
else:
    print("ko")
