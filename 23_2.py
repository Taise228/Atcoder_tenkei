MOD = 10 ** 9 + 7


def check(C, i, j):
    """check if the pattern j meets the condition on the row i"""

    k = 0
    while (j >> k) > 0:
        if (j >> k) & 1:
            if C[i][k] == '#':
                return False
        k += 1
    return True


def binary_compatible(j, k, W):
    """check if the patterns j and k are compatible"""

    k_patterns = []
    for i in range(W):
        if (k >> i) & 1:
            k_patterns.append(True)
        else:
            k_patterns.append(False)
    j_patterns = []
    for i in range(W):
        if (j >> i) & 1:
            j_patterns.append(True)
        else:
            j_patterns.append(False)

    for i in range(W):
        if j_patterns[i]:
            if k_patterns[i]:
                return False
            if i > 0 and k_patterns[i - 1]:
                return False
            if i < len(j_patterns) - 1 and k_patterns[i + 1]:
                return False
    return True


def main():
    H, W = map(int, input().split())
    C = []
    for _ in range(H):
        C.append(input())

    # bit DP
    opt = [[0 for _ in range(2 ** W)] for _ in range(H)]
    # opt[i][j]: the number of ways to fill the board till row i
    # when the row i is filled with the pattern j
    # (j is represented as a binary number)

    valid_patterns = []
    for p in range(2 ** W):
        i = p
        # check if i does not have a successive 1 in the binary representation
        i_patterns = []
        while i > 0:
            if i & 1:
                i_patterns.append(True)
            else:
                i_patterns.append(False)
            i >>= 1
        valid = True
        for j in range(len(i_patterns) - 1):
            if i_patterns[j] and i_patterns[j + 1]:
                valid = False
                break
        if valid:
            valid_patterns.append(p)

    # initialize
    for j in valid_patterns:
        if check(C, 0, j):
            opt[0][j] = 1

    # DP
    for i in range(1, H):
        for j in valid_patterns:
            if check(C, i, j):
                for k in valid_patterns:
                    if binary_compatible(j, k, W):
                        opt[i][j] += opt[i - 1][k]
                        opt[i][j] %= MOD

    # answer
    print(sum(opt[H - 1]) % MOD)


if __name__ == '__main__':
    main()
