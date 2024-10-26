def calculate_union_area(N, K, L):
    if K >= 2 * L:
        # Non-overlapping case
        return N * (2 * L) ** 2
    
    # Overlapping case
    intervals = []
    for i in range(N):
        center = i * K
        left = center - L
        right = center + L
        intervals.append((left, right))
    
    # Merge intervals
    intervals.sort()
    merged_intervals = []
    current_start, current_end = intervals[0]
    
    for start, end in intervals[1:]:
        if start <= current_end:
            current_end = max(current_end, end)
        else:
            merged_intervals.append((current_start, current_end))
            current_start, current_end = start, end
    
    merged_intervals.append((current_start, current_end))
    
    # Calculate the total area
    total_area = 0
    for start, end in merged_intervals:
        total_area += (end - start) * (2 * L)
    
    return total_area

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    N = int(data[0])
    K = int(data[1])
    L = int(data[2])
    
    result = calculate_union_area(N, K, L)
    print(result)

if __name__ == "__main__":
    main()