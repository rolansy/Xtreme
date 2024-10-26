def dfs(city, stars, graph, memo):
    if city in memo:
        return memo[city]
    
    max_length = 1  # At least the current city
    for neighbor in graph[city]:
        if stars[neighbor] > stars[city]:
            max_length = max(max_length, 1 + dfs(neighbor, stars, graph, memo))
    
    memo[city] = max_length
    return max_length

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])
    stars = list(map(int, data[1:N+1]))
    edges = data[N+1:]
    
    graph = [[] for _ in range(N)]
    for i in range(0, len(edges), 2):
        u = int(edges[i]) - 1
        v = int(edges[i+1]) - 1
        graph[u].append(v)
        graph[v].append(u)
    
    global max_restaurants
    max_restaurants = 0
    memo = {}
    
    for i in range(N):
        max_restaurants = max(max_restaurants, dfs(i, stars, graph, memo))
    
    print(max_restaurants)

if __name__ == "__main__":
    main()