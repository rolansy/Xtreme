import sys
import heapq
from collections import defaultdict, deque

input = sys.stdin.read

def main():
    data = input().split()
    N = int(data[0])
    M = int(data[1])
    
    group_ids = list(map(int, data[2:2 + N]))
    dependencies = data[2 + N:]
    
    adj_list = defaultdict(list)
    in_degree = [0] * N
    
    for i in range(M):
        A = int(dependencies[2 * i]) - 1
        B = int(dependencies[2 * i + 1]) - 1
        adj_list[A].append(B)
        in_degree[B] += 1
    
    # Priority queue to ensure lexicographical order
    pq = []
    for i in range(N):
        if in_degree[i] == 0:
            heapq.heappush(pq, (group_ids[i], i))
    
    result = []
    while pq:
        _, u = heapq.heappop(pq)
        result.append(u + 1)
        for v in adj_list[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                heapq.heappush(pq, (group_ids[v], v))
    
    if len(result) == N:
        print(" ".join(map(str, result)))
    else:
        print(-1)

if __name__ == "__main__":
    main()