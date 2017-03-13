MAX = 99999


def is_visited(m, x, y):
    return m[x][y]


def is_blocked(m, x, y):
    return m[x][y]


def is_wall(x, y, size):
    return x < 0 or x >= size or y < 0 or y >= size


def minimum(a, b, c, d):
    l = [a, b, c, d]
    min_val = min(l)
    return min_val


def get_shortest_path(m, row, col, x2, y2, visited):
    if is_wall(row, col, 4) \
            or is_blocked(m, row, col) \
            or is_visited(visited, row, col):
        return MAX
    if row == x2 and col == y2:
        return 0
    else:
        visited[row][col] = 1
        shortest_path = minimum(get_shortest_path(m, row-1, col, x2, y2, visited),
                                get_shortest_path(m, row, col-1, x2, y2, visited),
                                get_shortest_path(m, row+1, col, x2, y2, visited),
                                get_shortest_path(m, row, col+1, x2, y2, visited)
                                )+1
        visited[x1][y1] = 0
        return shortest_path

if __name__=='__main__':
    # print("Enter size of matrix")
    # size = int(raw_input())
    matrix = [[0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    visited = [[0 for i in xrange(4)] for j in xrange(4)]
    # matrix = raw_input()
    # x1, y1 = (int(x) for x in raw_input().split())
    x1, y1 = 0, 1
    x2, y2 = 3, 2
    print(get_shortest_path(matrix,x1,y1,x2,y2,visited))