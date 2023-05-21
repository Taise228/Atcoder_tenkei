H, W = map(int, input().split())

cells = []

for _ in range(H):
    cells.append(list(map(int, input().split())))

column = [0 for _ in range(H)]
row = [0 for _ in range(W)]

# column
for i in range(H):
    for j in range(W):
        column[i] += cells[i][j]
# row
for i in range(W):
    for j in range(H):
        row[i] += cells[j][i]

# answer
for i in range(H):
    for j in range(W):
        print(column[i] + row[j] - cells[i][j], end=" ")
    print("\n", end="")