import sys
input = sys.stdin.read

def generate_doubled_sequence(N):
    if N % 2 != 0:
        return -1
    sequence = [0] * (2 * N)
    for i in range(1, N + 1):
        sequence[i - 1] = i
        sequence[i - 1 + i] = i
    return sequence

def main():
    data = input().split()
    T = int(data[0])
    results = []
    for i in range(1, T + 1):
        N = int(data[i])
        result = generate_doubled_sequence(N)
        if result == -1:
            results.append("-1")
        else:
            results.append(" ".join(map(str, result)))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()