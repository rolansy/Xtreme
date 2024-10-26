MOD = 998244353

def count_ways(N, A, B):
    # Initialize DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    # Convert A and B to sets for quick lookup
    set_A = set(A)
    set_B = set(B)
    
    # Fill DP table
    for i in range(N + 1):
        for j in range(N + 1):
            if i + j == 0:
                continue
            current_num = i + j
            if current_num in set_A:
                if i > 0:
                    dp[i][j] = dp[i - 1][j]
            elif current_num in set_B:
                if j > 0:
                    dp[i][j] = dp[i][j - 1]
            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
                dp[i][j] %= MOD
    
    return dp[N][N]

def main():
    data = input().strip().split()
    
    N = int(data[0])
    X = int(data[1])
    A = list(map(int, data[2:2 + X]))
    Y = int(data[2 + X])
    B = list(map(int, data[3 + X:3 + X + Y]))
    
    result = count_ways(N, A, B)
    print(result)

main()