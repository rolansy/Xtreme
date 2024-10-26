import sys
import heapq

input = sys.stdin.read

def main():
    data = input().split()
    N = int(data[0])
    x = int(data[1])
    A = list(map(int, data[2:2 + N]))
    
    # Sort bricks in ascending order
    A.sort()
    
    # Priority queue to manage stacks
    stacks = []
    
    for brick in A:
        if stacks and stacks[0][0] <= brick - x:
            height, stack = heapq.heappop(stacks)
            stack.append(brick)
            heapq.heappush(stacks, (brick, stack))
        else:
            heapq.heappush(stacks, (brick, [brick]))
    
    # Output the results
    print(len(stacks))
    for _, stack in stacks:
        print(len(stack), ' '.join(map(str, reversed(stack))))

if __name__ == "__main__":
    main()