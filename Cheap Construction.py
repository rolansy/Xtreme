import sys
input = sys.stdin.read

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1
            self.count -= 1

def main():
    S = input().strip()
    N = len(S)
    results = [0] * N

    for length in range(1, N + 1):
        uf = UnionFind(N)
        seen = set()
        for i in range(N - length + 1):
            substring = S[i:i + length]
            if substring in seen:
                continue
            seen.add(substring)
            for j in range(i, i + length - 1):
                uf.union(j, j + 1)
        for k in range(1, N + 1):
            if results[k - 1] == 0 and uf.count == k:
                results[k - 1] = length

    print(" ".join(map(str, results)))

if __name__ == "__main__":
    main()