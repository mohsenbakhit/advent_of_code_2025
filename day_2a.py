import sys

def is_invalid(s: int) -> bool:
    n = str(s)
    length = len(n)
    if length % 2 != 0:
        return False
    
    mid = length // 2
    return n[:mid] == n[mid:]

if len(sys.argv) > 1:
    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            total = 0
            input = file.read().replace('\n','').split(',')
            ranges = [x.split('-') for x in input]
            for start,end in ranges:
                for num in range(int(start), int(end) + 1):
                    if is_invalid(num):
                        total += int(num)

            print(total)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error reading file: {e}")
