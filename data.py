import requests;

def decode_message(doc_url):
    # Step 1: Fetch the Google Doc content
    response = requests.get(doc_url)
    response.raise_for_status()  # Ensure the request was successful
    content = response.text.splitlines()
    
    # Step 2: Parse the data into a list of (character, x, y)
    data = []
    for line in content:
        parts = line.split(',')
        char = parts[0].strip()
        x = int(parts[1].strip())
        y = int(parts[2].strip())
        data.append((char, x, y))
    
    # Step 3: Determine grid dimensions
    max_x = max(item[1] for item in data)
    max_y = max(item[2] for item in data)
    
    # Step 4: Create an empty grid
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Step 5: Fill the grid with characters
    for char, x, y in data:
        grid[y][x] = char
    
    # Step 6: Print the grid row by row, ensuring proper alignment
    for row in grid:
        print(''.join(row).rstrip())

# Example usage
doc_url = "https://docs.google.com/document/u/0/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub?pli=1"
decode_message(doc_url)
