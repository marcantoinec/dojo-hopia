def print_grid(grid):
    for row in grid:
        for element in row:
            if element == 0:
                print(".", end=" ")
            else:
                print(element, end=" ")
        print()


print_grid([[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 2048, 0, 0],
            [0, 0, 0, 0]])