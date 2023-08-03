MOD = 10 ** 9 + 7


def check(log, i, j):
    """check if the cell (i, j) is available to put a block
    Args:
        log (list): log of the board
        i (int): row number
        j (int): column number

    Returns:
        bool: True if the cell is available
    """
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dir in dirs:
        x = i + dir[0]
        y = j + dir[1]
        if 0 <= x < len(log) and 0 <= y < len(log[0]) and log[x][y]:
            return False
    return True


def backtrack_search(C, log, i, j, H, W):
    while (C[i][j] == '#') or (check(log, i, j) is False):
        j += 1
        if j == W:
            i += 1
            j = 0
            if i == H:
                return 1

    count = 0
    next_i = i
    next_j = j + 1
    if next_j == W:
        next_i += 1
        next_j = 0

    if next_i == H:
        if check(log, i, j):
            return 2
        else:
            return 1

    if check(log, i, j):
        log[i][j] = True
        count += backtrack_search(C, log, next_i, next_j, H, W)
        log[i][j] = False
        count += backtrack_search(C, log, next_i, next_j, H, W)
    else:
        count += backtrack_search(C, log, next_i, next_j, H, W)

    return count % MOD


def main():
    H, W = map(int, input().split())
    C = []
    for _ in range(H):
        C.append(input())

    # backtracking
    log = [[False] * W for _ in range(H)]
    print(backtrack_search(C, log, 0, 0, H, W))


if __name__ == '__main__':
    main()
