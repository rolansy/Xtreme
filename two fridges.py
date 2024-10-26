def find_fridge_temperatures(N, intervals):
    if N == 0:
        return (0, 0)  # Any valid temperature pair

    for T1 in range(-100, 101):
        for T2 in range(T1, 101):
            valid = True
            for (a, b) in intervals:
                if not (a <= T1 <= b or a <= T2 <= b):
                    valid = False
                    break
            if valid:
                return (T1, T2)
    
    return -1

# Read input
import sys
input = sys.stdin.read
data = input().strip().split()

if len(data) == 0:
    print(-1)
else:
    N = int(data[0])
    intervals = [(int(data[i]), int(data[i+1])) for i in range(1, len(data), 2)]

    # Find and print the result
    result = find_fridge_temperatures(N, intervals)
    if result == -1:
        print(result)
    else:
        print(result[0], result[1])