from collections import defaultdict
import time

N = int(input())

start = time.time()

al = defaultdict(list)   #adjacency list

for _ in range(N-1):
    a, b = map(int, input().split())
    al[a].append(b)
    al[b].append(a)

print("1", time.time() - start)

#spanning tree に辺を一つ加えてできるcycleの中で一番長いものの長さを求める
#まず任意に頂点をとる。その末端から一番遠いところ(これは末端)が、一番長いcycleに含まれる
end = 1

#verted end からの距離を全ての点に対して求め、そのmaxの点を求める
#BFS
cost = [-1 for _ in range(N)]
seen = [False for _ in range(N)]
qu = [end]
cost[end-1] = 0
while len(qu) != 0:
    vertex = qu.pop(0)
    if seen[vertex-1]:
        continue
    seen[vertex-1] = True
    for adj in al[vertex]:
        if seen[adj-1]:
            continue
        if cost[adj-1] == -1:
            cost[adj-1] = cost[vertex-1] + 1
        qu.append(adj)
        
max_vertex = 1
for i in range(1, N):
    if cost[i] > cost[max_vertex-1]:
        max_vertex = i+1

print("2", time.time() - start)

# max_vertex を起点としてまたBFS
cost = [-1 for _ in range(N)]
seen = [False for _ in range(N)]
qu = [max_vertex]
cost[max_vertex-1] = 0
while len(qu) != 0:
    vertex = qu.pop(0)
    if seen[vertex-1]:
        continue
    seen[vertex-1] = True
    for adj in al[vertex]:
        if seen[adj-1]:
            continue
        if cost[adj-1] == -1:
            cost[adj-1] = cost[vertex-1] + 1
        qu.append(adj)

print("3", time.time() - start)

print(max(cost) + 1)