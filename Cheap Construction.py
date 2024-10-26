def suffix_array_construction(s):
    n = len(s)
    suffix_array = sorted(range(n), key=lambda i: s[i:])
    rank = [0] * n
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i
    k = 1
    while k < n:
        key = lambda i: (rank[i], rank[i + k] if i + k < n else -1)
        suffix_array.sort(key=key)
        tmp = [0] * n
        for i in range(1, n):
            tmp[suffix_array[i]] = tmp[suffix_array[i - 1]] + (key(suffix_array[i - 1]) < key(suffix_array[i]))
        rank = tmp
        k *= 2
    return suffix_array

def lcp_array_construction(s, suffix_array):
    n = len(s)
    rank = [0] * n
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i
    lcp = [0] * n
    h = 0
    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1
    return lcp

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        self.count = n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            self.count -= 1

def find_min_length_for_k_components(s, k):
    n = len(s)
    suffix_array = suffix_array_construction(s)
    lcp = lcp_array_construction(s, suffix_array)
    
    uf = UnionFind(n)
    lcp_with_index = sorted((lcp[i], i) for i in range(1, n))
    
    component_count = n
    for length, i in lcp_with_index:
        if length == 0:
            continue
        if uf.find(suffix_array[i]) != uf.find(suffix_array[i - 1]):
            uf.union(suffix_array[i], suffix_array[i - 1])
            component_count -= 1
        if component_count == k:
            return length
    return 0

def main():
    import sys
    input = sys.stdin.read
    s = input().strip()
    n = len(s)
    
    results = []
    for k in range(1, n + 1):
        results.append(find_min_length_for_k_components(s, k))
    
    print(" ".join(map(str, results)))

if __name__ == "__main__":
    main()