import sys

def max_joltage(bank: str) -> int:
    result = []
    start = 0
    
    for pos in range(12):
        remaining = 11 - pos
        end = len(bank) - remaining
        
        max_digit = max(bank[start:end])
        max_idx = bank.index(max_digit, start, end)
        
        result.append(max_digit)
        start = max_idx + 1
    
    return int(''.join(result))

if len(sys.argv) :
    filename = sys.argv[1]
    try:    
        with open(filename, 'r') as file:
            total_joltage = 0
            for line in file:
                total_joltage += max_joltage(line.replace('\n',''))
            
        print(f"total_joltage: {total_joltage}")
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    except Exception as e:
        print(f"Error: Could not read file: {e}")

