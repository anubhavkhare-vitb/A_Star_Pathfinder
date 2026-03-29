from astar import astar

def print_grid(grid, path=None):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if path and (i, j) in path:
                print("*", end=" ")
            elif grid[i][j] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()


def get_grid():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    grid = []
    print("Enter grid row by row (0 = free, 1 = obstacle):")

    for i in range(rows):
        row = list(map(int, input().split()))
        grid.append(row)

    return grid


def get_point(name):
    x = int(input(f"Enter {name} row: "))
    y = int(input(f"Enter {name} column: "))
    return (x, y)


def main():
    print("=== A* Pathfinding (Interactive CLI) ===")

    grid = get_grid()

    start = get_point("START")
    goal = get_point("GOAL")

    print("\nGrid:")
    print_grid(grid)

    path = astar(grid, start, goal)

    if path:
        print("\nPath Found:")
        print(path)

        print("\nVisual Path:")
        print_grid(grid, path)
    else:
        print("No path found")


if __name__ == "__main__":
    main()