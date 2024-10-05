n = int(input())
p = list(map(int, input().split()))


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        if self.rank[p_root] < self.rank[q_root]:
            self.parent[p_root] = q_root
        elif self.rank[p_root] > self.rank[q_root]:
            self.parent[q_root] = p_root
        else:
            self.parent[q_root] = p_root
            self.rank[p_root] += 1


for i in range(n):
    p[i] -= 1

uf = UnionFind(n)

for i in range(n):
    uf.union(p[i], i)

# trees =  len(set(uf.parent))

roots = set()
for i in range(n):
    roots.add(uf.find(i))

trees = len(roots)
print(trees)