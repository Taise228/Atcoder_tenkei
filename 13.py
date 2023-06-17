import heapq


def main():
    INF = float('inf')

    N, M = map(int, input().split())
    costs = {}
    edges = [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        costs[(a - 1, b - 1)] = c
        costs[(b - 1, a - 1)] = c
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)

    # dijkstra from 0
    # use heap
    dist = [INF for _ in range(N)]
    dist[0] = 0
    heap = [(dist[i], i) for i in range(N)]
    heapq.heapify(heap)
    U = set([i for i in range(N)])
    while len(U) > 0:
        d, v = heapq.heappop(heap)
        if v not in U:
            continue
        U.remove(v)
        if dist[v] < d:
            continue
        for u in edges[v]:
            if u in U and dist[u] > dist[v] + costs[(v, u)]:
                dist[u] = dist[v] + costs[(v, u)]
                heapq.heappush(heap, (dist[u], u))

    # diskstra from N - 1
    # use heap
    dist2 = [INF for _ in range(N)]
    dist2[N - 1] = 0
    heap = [(dist2[i], i) for i in range(N)]
    heapq.heapify(heap)
    U = set([i for i in range(N)])
    while len(U) > 0:
        d, v = heapq.heappop(heap)
        if v not in U:
            continue
        U.remove(v)
        if dist2[v] < d:
            continue
        for u in edges[v]:
            if u in U and dist2[u] > dist2[v] + costs[(v, u)]:
                dist2[u] = dist2[v] + costs[(v, u)]
                heapq.heappush(heap, (dist2[u], u))

    # print answer
    for i in range(N):
        if 0 < i < N - 1:
            print(dist[i] + dist2[i])
        else:
            print(dist[N - 1])


if __name__ == '__main__':
    main()
