def laser_defense(L, N, M, beams_A, beams_B):
    # Store the coordinates of the beams
    beams_A_U = []
    beams_A_R = []
    beams_B_U = []
    beams_B_L = []
    
    for beam in beams_A:
        if beam[0] == 'U':
            beams_A_U.append(beam[1])
        elif beam[0] == 'R':
            beams_A_R.append(beam[1])
    
    for beam in beams_B:
        if beam[0] == 'U':
            beams_B_U.append(beam[1])
        elif beam[0] == 'L':
            beams_B_L.append(beam[1])
    
    # Coordinate compression
    all_coords = set(beams_A_U + beams_A_R + beams_B_U + beams_B_L)
    all_coords = sorted(all_coords)
    coord_map = {coord: idx for idx, coord in enumerate(all_coords)}
    
    # Count intersections
    intersections = set()
    for u in beams_A_U:
        for l in beams_B_L:
            intersections.add((coord_map[u], coord_map[l]))
    for r in beams_A_R:
        for u in beams_B_U:
            intersections.add((coord_map[r], coord_map[u]))
    
    # Calculate the number of areas
    num_areas = (len(beams_A_U) + 1) * (len(beams_B_L) + 1) + (len(beams_A_R) + 1) * (len(beams_B_U) + 1) - len(intersections)
    
    return num_areas

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    L = int(data[0])
    N = int(data[1])
    M = int(data[2])
    
    beams_A = []
    beams_B = []
    
    index = 3
    for _ in range(N):
        direction = data[index]
        coord = int(data[index + 1])
        beams_A.append((direction, coord))
        index += 2
    
    for _ in range(M):
        direction = data[index]
        coord = int(data[index + 1])
        beams_B.append((direction, coord))
        index += 2
    
    result = laser_defense(L, N, M, beams_A, beams_B)
    print(result)

if __name__ == "__main__":
    main()