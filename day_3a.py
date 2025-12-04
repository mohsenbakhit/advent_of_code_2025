import sys



if len(sys.argv > 1):
    filename = sys.argv[1]
    try:    
        with open(filename, 'r') as file:
    
    except FileNotFoundError:
        print(f"Error: File {filename} not found")
    except Exception as e:
        print(f"Error: Could not read file: {e}")

