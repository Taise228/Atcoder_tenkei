def main():
    N, M = map(int, input().split())

    edges = []
    for _ in range(M):
        l, r = map(int, input().split())
        edges.append([l, r])

    # brute force
    edges.sort()
    ans = 0
    for i in range(M):
        for j in range(i+1, M):
            small_i = min(edges[i])
            large_i = max(edges[i])
            small_j = min(edges[j])
            large_j = max(edges[j])
            if small_i < small_j < large_i < large_j:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
