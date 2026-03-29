import heapq

class Node:
    def __init__(self, position, g=0, h=0, parent=None):
        self.position = position
        self.g = g  # cost from start
        self.h = h  # heuristic cost to goal
        self.f = g + h
        self.parent = parent

    def __lt__(self, other):
        return self.f < other.f


def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(pos, grid):
    neighbors = []
    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    for d in directions:
        new_pos = (pos[0] + d[0], pos[1] + d[1])

        if (0 <= new_pos[0] < len(grid) and
            0 <= new_pos[1] < len(grid[0]) and
            grid[new_pos[0]][new_pos[1]] != 1):

            neighbors.append(new_pos)

    return neighbors


def reconstruct_path(node):
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    return path[::-1]


def astar(grid, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)

        if current.position == goal:
            return reconstruct_path(current)

        closed_set.add(current.position)

        for neighbor in get_neighbors(current.position, grid):
            if neighbor in closed_set:
                continue

            g = current.g + 1
            h = heuristic(neighbor, goal)
            neighbor_node = Node(neighbor, g, h, current)

            heapq.heappush(open_list, neighbor_node)

    return None