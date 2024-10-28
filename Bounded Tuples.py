import sys
input = sys.stdin.read

MOD = 998244353

def main():
    data = input().split()
    index = 0
    N = int(data[index])
    M = int(data[index + 1])
    index += 2
    
    constraints = []
    for _ in range(M):
        low = int(data[index])
        high = int(data[index + 1])
        K = int(data[index + 2])
        indices = list(map(int, data[index + 3:index + 3 + K]))
        constraints.append((low, high, indices))
        index += 3 + K
    
    # Initialize DP table
    dp = {}
    dp[0] = 1  # Base case: one way to assign zero to all variables
    
    # Iterate over all possible subsets of variables
    for mask in range(1 << N):
        if mask not in dp:
            continue
        current_sum = dp[mask]
        
        # Try to add each variable to the current subset
        for i in range(N):
            if mask & (1 << i) == 0:
                new_mask = mask | (1 << i)
                if new_mask not in dp:
                    dp[new_mask] = 0
                dp[new_mask] = (dp[new_mask] + current_sum) % MOD
    
    # Check constraints
    def check_constraints(mask):
        for low, high, indices in constraints:
            subset_sum = sum((mask >> (i - 1)) & 1 for i in indices)
            if not (low <= subset_sum <= high):
                return False
        return True
    
    # Count valid assignments
    valid_count = 0
    for mask in range(1 << N):
        if check_constraints(mask):
            valid_count = (valid_count + dp[mask]) % MOD
    
    print(valid_count)

if __name__ == "__main__":
    main()