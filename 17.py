def main():
    N, M = map(int, input().split())

    edges = []
    count = [0 for _ in range(N + 1)]
    for _ in range(M):
        l, r = map(int, input().split())
        edges.append([l, r])
        count[l] += 1

    edges.sort()
    """# brute force
    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            small_i = edges[i][0]
            large_i = edges[i][1]
            small_j = edges[j][0]
            large_j = edges[j][1]
            if small_i < small_j < large_i < large_j:
                ans += 1"""

    # accumulate with L
    acc_count = [0 for _ in range(N + 1)]
    for i in range(1, N + 1):
        acc_count[i] = acc_count[i - 1] + count[i]

    # subtract incident from all the patterns
    ans = (N * (N + 1)) // 2

    for i in range(1, N + 1):
        count_i = count[i]
        ans -= (count_i * (count_i + 1)) // 2

    for i in range(M):
        R = edges[i][1]
        ans -= M - acc_count[R - 1]

    # subtract cases when L_i < L_j < R_j < R_i
    # TODO

    print(ans)


if __name__ == '__main__':
    main()
