from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


def main():
    H, W = map(int, input().split())
    grid = [[0 for _ in range(W)] for _ in range(H)]
    uf = UnionFind(H * W)

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            grid[query[1] - 1][query[2] - 1] = 1
            for d in dirs:
                if 0 <= query[1] - 1 + d[0] < H and 0 <= query[2] - 1 + d[1] < W:
                    if grid[query[1] - 1 + d[0]][query[2] - 1 + d[1]] == 1:
                        uf.union((query[1] - 1) * W + query[2] - 1, (query[1] - 1 + d[0]) * W + query[2] - 1 + d[1])
        else:
            if grid[query[1] - 1][query[2] - 1] == 1 and grid[query[3] - 1][query[4] - 1] == 1:
                if uf.same((query[1] - 1) * W + query[2] - 1, (query[3] - 1) * W + query[4] - 1):
                    print('Yes')
                else:
                    print('No')
            else:
                print('No')


if __name__ == '__main__':
    main()
