import requests
from bs4 import BeautifulSoup


def fetch_google_doc(url):
    """Fetches the HTML content from a Google Doc URL."""
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def parse_table(html):
    """Parses the HTML table and extracts (x, y, character) values."""
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')
    # headers = [col.text.strip() for col in rows[0].find_all('td')]
    # print(f"Table headers:\n{headers}\n")
    grid_data = []
    for row in rows[1:]:
        cols = row.find_all('td')
        if len(cols) < 3:
            continue
        x = int(cols[0].text.strip())
        char_elem = cols[1].find('span')
        char = char_elem.text.strip() if char_elem else cols[1].text.strip()
        y = int(cols[2].text.strip())
        grid_data.append((char, x, y))
    return grid_data

def build_grid(grid_data):
    """Builds a 2D grid where (0,0) is the TOP-LEFT corner, Y increases downward."""
    min_x = min(x for _, x, _ in grid_data)
    max_x = max(x for _, x, _ in grid_data)
    min_y = min(y for _, _, y in grid_data)
    max_y = max(y for _, _, y in grid_data)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    grid = [[' ' for _ in range(width)] for _ in range(height)]
    for char, x, y in grid_data:
        grid[max_y - y][x - min_x] = char
    return grid

def print_table(grid_data):
    """Prints the extracted table in (X, Y, Character) format with aligned columns."""
    print("Extracted Table:")
    print("-" * 20)
    for char, x, y in sorted(grid_data, key=lambda item: (item[2], item[1])):  
        print(f"{x:<5} {char:<5} {y:<5}")

def print_grid(grid):
    """Prints the grid from top to bottom, keeping (0,0) at the TOP-LEFT."""
    for row in grid:
        print("".join(row))

def draw_secret_symbol(grid_data):
    """Builds and prints the secret symbol from coordinate data."""
    grid = build_grid(grid_data)
    print("\nSecret Symbol:\n")
    print_grid(grid)

def process_google_doc(url):
    """Main function to fetch, parse, build, and print the character grid."""
    html_data = fetch_google_doc(url)
    grid_data = parse_table(html_data)
    # print_table(grid_data)
    draw_secret_symbol(grid_data)


#google_doc_url = "https://docs.google.com/document/u/0/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub?pli=1"
google_doc_url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
process_google_doc(google_doc_url)
