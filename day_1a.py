import sys
if len(sys.argv) > 1:
    filename = sys.argv[1]
    print(f"Reading from file: {filename}")
    try:
        with open(filename, 'r') as file:
            cur_pos = 50
            password = 0
            for line in file:
                line = line.strip()
                if not line:
                    continue
                direction = line[0]
                distance = int(line[1:])
            
                if direction == "L":
                    cur_pos = (cur_pos - distance) % 100
                elif direction == "R":
                    cur_pos = (cur_pos + distance) % 100
            
                if cur_pos == 0:
                    password += 1
            
            print(f"Password is {password}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error reading file: {e}")