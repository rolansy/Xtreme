import sys
import math
from itertools import combinations

input = sys.stdin.read

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def main():
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    elasticities = list(map(int, data[2:2 + K]))
    
    total_hit_tiles = 0
    
    # Inclusion-Exclusion Principle
    for i in range(1, K + 1):
        for combo in combinations(elasticities, i):
            lcm_value = combo[0]
            for e in combo[1:]:
                lcm_value = lcm(lcm_value, e)
                if lcm_value > N:
                    break
            if lcm_value > N:
                continue
            count = N // lcm_value
            if i % 2 == 1:
                total_hit_tiles += count
            else:
                total_hit_tiles -= count
    
    print(total_hit_tiles)

if __name__ == "__main__":
    main()