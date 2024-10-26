import struct

def hex_to_float(hex_str):
    return struct.unpack('!f', bytes.fromhex(hex_str))[0]

def float_to_hex(f):
    return format(struct.unpack('!I', struct.pack('!f', f))[0], '08x')

def execute_commands(C0, LUTs, commands):
    results = [hex_to_float(C0)]
    
    for command in commands:
        parts = command.split()
        if parts[0] == 'C':
            results.append(hex_to_float(parts[1]))
        elif parts[0] == 'N':
            i = int(parts[1])
            j = int(parts[2])
            nand_result = ~(struct.unpack('!I', struct.pack('!f', results[i]))[0] & struct.unpack('!I', struct.pack('!f', results[j]))[0]) & 0xFFFFFFFF
            results.append(struct.unpack('!f', struct.pack('!I', nand_result))[0])
        elif parts[0] == 'F':
            i = int(parts[1])
            j = int(parts[2])
            k = int(parts[3])
            fma_result = results[i] * results[j] + results[k]
            results.append(fma_result)
        elif parts[0] == 'L':
            i = int(parts[1])
            j = int(parts[2])
            b = int(parts[3])
            mask = (struct.unpack('!I', struct.pack('!f', results[0]))[0] >> (32 - j - b)) & ((1 << b) - 1)
            results.append(hex_to_float(LUTs[i][mask]))
    
    return float_to_hex(results[-1])

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        C0 = data[index]
        index += 1
        L = int(data[index])
        index += 1
        
        LUTs = []
        for _ in range(L):
            k = int(data[index])
            index += 1
            LUT = data[index:index + (1 << k)]
            LUTs.append(LUT)
            index += (1 << k)
        
        Q = int(data[index])
        index += 1
        
        commands = []
        for _ in range(Q):
            commands.append(data[index])
            index += 1
            if commands[-1][0] == 'L':
                commands[-1] += ' ' + data[index] + ' ' + data[index + 1]
                index += 2
            elif commands[-1][0] in {'N', 'F'}:
                commands[-1] += ' ' + data[index] + ' ' + data[index + 1]
                index += 2
        
        result = execute_commands(C0, LUTs, commands)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()