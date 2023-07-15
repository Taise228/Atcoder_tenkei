import sys


def dfs(edges, visited, order, v):
    visited[v] = True
    for u in edges[v]:
        if not visited[u]:
            dfs(edges, visited, order, u)
            visited[u] = True
    order.append(v)


def main():
    N, M = map(int, input().split())

    edges = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        edges[a - 1].add(b - 1)

    # find SCC
    # first, find order of vertices according to DFS finish time
    visited = [False for _ in range(N)]
    order = []
    for v in range(N):
        if not visited[v]:
            dfs(edges, visited, order, v)

    # reverse edges
    rev_edges = [[] for _ in range(N)]
    for v in range(N):
        for u in edges[v]:
            rev_edges[u].append(v)

    # find SCC
    visited = [False for _ in range(N)]
    scc = []
    for v in reversed(order):
        if not visited[v]:
            scc.append([])
            dfs(rev_edges, visited, scc[-1], v)

    # count the number of pairs of vertices in the same SCC
    ans = 0
    for c in scc:
        ans += len(c) * (len(c) - 1) // 2

    print(ans)


if __name__ == '__main__':
    sys.setrecursionlimit(10 ** 5 + 1)
    main()
