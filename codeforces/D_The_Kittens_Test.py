n = int(input())
border_removed = []

for _ in range(n - 1):
    x, y = map(int, input().split())
    border_removed.append((x, y))

# prev = [-1] * (n + 1)
# next = [-1] * (n + 1)

# def find_end(k, direction):
#     if direction == "next":
#         while next[k] != -1:
#             k = next[k]
#         return k
#     elif direction == "prev":
#         while prev[k] != -1:
#             k = prev[k]
#         return k

# for xi, yi in border_removed:
#     xi_end = find_end(xi, "next")
#     yi_start = find_end(yi, "prev")

#     next[xi_end] = yi_start
#     prev[yi_start] = xi_end

# start = 1
# while prev[start] != -1:
#     start = prev[start]

# arrangement = []
# while start != -1:
#     arrangement.append(start)
#     start = next[start]

# print(" ".join(map(str, arrangement)))

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.left = list(range(n + 1))
        self.right = list(range(n + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
                self.left[root_x] = min(self.left[root_x], self.left[root_y])
                self.right[root_x] = max(self.right[root_x], self.right[root_y])
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
                self.left[root_y] = min(self.left[root_x], self.left[root_y])
                self.right[root_y] = max(self.right[root_x], self.right[root_y])
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
                self.left[root_x] = min(self.left[root_x], self.left[root_y])
                self.right[root_x] = max(self.right[root_x], self.right[root_y])

uf = UnionFind(n)

for x, y in border_removed:
    uf.union(x, y)

start = uf.left[uf.find(1)]
arrangement = []

current = start
while current != -1:
    arrangement.append(current)
    next_kitten = uf.right[uf.find(current)]
    if next_kitten == current:
        current = -1
    else:
        current = next_kitten + 1

print(" ".join(map(str, arrangement)))
