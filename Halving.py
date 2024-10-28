MOD = 998244353

def count_valid_permutations(N, C, R, B):
    from itertools import combinations
    
    # Identify fixed and unfixed elements
    fixed = [c for c in C if c != -1]
    unfixed_positions = [i for i, c in enumerate(C) if c == -1]
    all_elements = set(range(1, 2 * N + 1))
    unfixed_elements = list(all_elements - set(fixed))
    
    # Initialize DP table
    dp = [[0] * (1 << len(unfixed_elements)) for _ in range(N + 1)]
    dp[0][0] = 1
    
    # Precompute pairs
    pairs = [(i, j) for i in range(len(unfixed_elements)) for j in range(i + 1, len(unfixed_elements))]
    
    for i in range(N):
        for mask in range(1 << len(unfixed_elements)):
            if dp[i][mask] == 0:
                continue
            
            for (u, v) in pairs:
                if (mask & (1 << u)) or (mask & (1 << v)):
                    continue
                
                a1, a2 = unfixed_elements[u], unfixed_elements[v]
                if R[i] == 0:
                    if min(a1, a2) == B[i]:
                        new_mask = mask | (1 << u) | (1 << v)
                        dp[i + 1][new_mask] = (dp[i + 1][new_mask] + dp[i][mask]) % MOD
                else:
                    if max(a1, a2) == B[i]:
                        new_mask = mask | (1 << u) | (1 << v)
                        dp[i + 1][new_mask] = (dp[i + 1][new_mask] + dp[i][mask]) % MOD
    
    # Sum up valid configurations
    result = 0
    for mask in range(1 << len(unfixed_elements)):
        result = (result + dp[N][mask]) % MOD
    
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    C = list(map(int, data[1:2 * N + 1]))
    R = list(map(int, data[2 * N + 1:3 * N + 1]))
    B = list(map(int, data[3 * N + 1:4 * N + 1]))
    
    result = count_valid_permutations(N, C, R, B)
    print(result)

if __name__ == "__main__":
    main()