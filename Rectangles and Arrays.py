import sys
input = sys.stdin.read

def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Sentinel value to pop all elements from the stack at the end
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    heights.pop()  # Remove the sentinel value
    return max_area

def main():
    data = input().split()
    N = int(data[0])
    X = int(data[1])
    A = list(map(int, data[2:2 + N]))
    
    # Calculate the maximum area without any modification
    max_area = largest_rectangle_area(A)
    
    # Calculate the maximum area with one modification
    for i in range(N):
        if A[i] != X:
            original_value = A[i]
            A[i] = X
            max_area = max(max_area, largest_rectangle_area(A))
            A[i] = original_value
    
    print(max_area)

if __name__ == "__main__":
    main()