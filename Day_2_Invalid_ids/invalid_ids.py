import requests
import os
import sys


SESSION_COOKIE = '53616c7465645f5f257629c68340882a2f4c9317038ad7f407056d54347ba68f01d68f96295d4e2e01cedc40620aa58d796a708084a85ec680e433c996b3c924' 
YEAR = 2025

## Get inputs for Advent of Code problems
def get_aoc_input(day, session_cookie):

    filename = f"input_day_{day}.txt"
    
    # Check local path for file
    if os.path.exists(filename):
        print(f"[{filename}] found locally. Reading...")
        with open(filename, 'r') as f:
            return f.readlines()

    # If not found, download 
    print(f"[{filename}] not found. Downloading from server...")
    if not session_cookie in session_cookie:
        print("Error: Session cookie is missing!")
        sys.exit(1)

    url = f"https://adventofcode.com/{YEAR}/day/{day}/input"
    headers = {
        'Cookie': f'session={session_cookie}',
        'User-Agent': 'github.com/user/repo by user@email.com'
    }

    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

    # Save to local
    with open(filename, 'w') as f:
        f.write(response.text)
      

def is_invalid_id(number):
    """
    Checks if a number is formed by a sequence of digits repeated twice.
    Example: 123123 (True), 55 (True), 121 (False - odd length)
    """
    s = str(number)
    length = len(s)
    
    # Optimization: Odd length numbers cannot be split into two equal halves
    if length % 2 != 0:
        return False
        
    mid = length // 2
    return s[:mid] == s[mid:]


def solve_day_2(input_lines):
    """
    Takes the list of lines from get_aoc_input, parses ranges, 
    and sums the invalid IDs.
    """
    # Join all lines into one string and remove newlines
    full_text = "".join(input_lines).replace('\n', '').strip()
    
    # Split into individual ranges
    ranges = full_text.split(',')
    
    total_invalid_sum = 0
    count = 0
    
    for r in ranges:
        if not r: 
            continue # Skip empty
        
        try:
            start_str, end_str = r.split('-')
            start = int(start_str)
            end = int(end_str)
        except ValueError:
            print(f"Skipping malformed range: {r}")
            continue

        # Optimization: If the range is purely odd-digit numbers (e.g., 100-999), skip it entirely.
        # This works if the range doesn't cross a digit boundary (e.g. 99-100).
        if len(start_str) == len(end_str) and len(start_str) % 2 != 0:
            continue

        # 3. Check numbers in the range
        for num in range(start, end + 1):
            if is_invalid_id(num):
                total_invalid_sum += num
                count += 1
                
    return total_invalid_sum

if __name__ == "__main__":
    day_data = get_aoc_input(2, SESSION_COOKIE)

    result = solve_day_2(day_data)
    
    print(f"Total Sum of Invalid IDs: {result}")