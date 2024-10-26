class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index

    def query(self, index):
        sum = 0
        while index > 0:
            sum += self.tree[index]
            index -= index & -index
        return sum

    def range_update(self, left, right, delta):
        self.update(left, delta)
        self.update(right + 1, -delta)

    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    N = int(data[index])
    Q = int(data[index + 1])
    index += 2

    P = list(map(int, data[index:index + N]))
    index += N

    fenwick_tree = FenwickTree(N)
    fenwick_tree_perm = FenwickTree(N)
    results = []

    for _ in range(Q):
        T = int(data[index])
        if T == 0 or T == 1:
            l = int(data[index + 1])
            r = int(data[index + 2])
            c = int(data[index + 3])
            if T == 0:
                fenwick_tree.range_update(l, r, c)
            else:
                for i in range(l, r + 1):
                    fenwick_tree_perm.update(P[i - 1], c)
            index += 4
        elif T == 2 or T == 3:
            l = int(data[index + 1])
            r = int(data[index + 2])
            if T == 2:
                results.append(fenwick_tree.range_query(l, r))
            else:
                sum = 0
                for i in range(l, r + 1):
                    sum += fenwick_tree_perm.query(P[i - 1])
                results.append(sum)
            index += 3

    for result in results:
        print(result)

if __name__ == "__main__":
    main()