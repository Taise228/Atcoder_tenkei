def main():
    N = int(input())

    edges = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        edges[u - 1].append(v - 1)
        edges[v - 1].append(u - 1)

    # find (2 / N) nodes such that no two are connected by an edge
    # guaranteed that N is even
    # also this is a tree, which means that there is no cycle and all the nodes are connected

    # BFS
    # depth[i] = depth of node i
    depth = [-1] * N
    depth[0] = 0
    queue = [0]
    pos = 0
    while pos < len(queue):
        u = queue[pos]
        pos += 1
        for v in edges[u]:
            if depth[v] != -1:
                continue
            else:
                depth[v] = depth[u] + 1
                queue.append(v)

    even = []
    odd = []
    for i in range(N):
        if depth[i] % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    if len(even) >= len(odd):
        for i in range(N // 2):
            print(even[i] + 1, end=' ')
    else:
        for i in range(N // 2):
            print(odd[i] + 1, end=' ')
    print()


if __name__ == '__main__':
    main()
