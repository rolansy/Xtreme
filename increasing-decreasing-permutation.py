from itertools import permutations

def min_swaps_to_sort(arr):
    n = len(arr)
    arrpos = [*enumerate(arr)]
    arrpos.sort(key=lambda it: it[1])
    vis = {k: False for k in range(n)}
    ans = 0
    for i in range(n):
        if vis[i] or arrpos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = arrpos[j][0]
            cycle_size += 1
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    M = int(data[1])
    
    # Generate all permutations of length N
    perms = list(permutations(range(1, N + 1)))
    
    # Define the target permutation
    mid = (N + 1) // 2
    target = list(range(1, mid + 1)) + list(range(N, mid, -1))
    
    total_swaps = 0
    
    for perm in perms:
        perm_list = list(perm)
        target_list = list(target)
        # Count the number of swaps to transform perm into target
        inversions = min_swaps_to_sort([perm_list.index(x) for x in target_list])
        total_swaps += inversions
        total_swaps %= M
    
    print(total_swaps)

if __name__ == "__main__":
    main()