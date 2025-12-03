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
        
    return response.text.strip().split('\n')


def solve_day_1(data):
    current_pos = 50
    zero_hits = 0
    
    for line in data:
        line = line.strip()
        if not line: continue
        
        direction = line[0]
        distance = int(line[1:])
        
        if direction == 'R':
            current_pos = (current_pos + distance) % 100
        elif direction == 'L':
            current_pos = (current_pos - distance) % 100
            
        if current_pos == 0:
            zero_hits += 1
            
    return zero_hits

def solve_day_1_part_2(data):

    current_pos = 50
    total_zero_hits = 0

    for line in data:
        line = line.strip()
        if not line:
            continue
        direction = line[0]
        distance = int(line[1:])

        total_zero_hits += (distance // 100)

        remainder = distance % 100

        for _ in range(remainder):
            if direction == 'R':
                current_pos = (current_pos + 1) % 100
            elif direction == 'L':
                current_pos = (current_pos - 1) % 100

            if current_pos == 0:
                total_zero_hits += 1

    return total_zero_hits


if __name__ == "__main__":
    day_data = get_aoc_input(1, SESSION_COOKIE)
    
    part1_answer = solve_day_1(day_data)

    part2_answer = solve_day_1_part_2(day_data)

    
    print("-" * 30)
    print(f"Day 1 Answer Part 1: {part1_answer}")
    print("-" * 30)

    print("-" * 30)
    print(f"Day 1 Answer Part 2: {part2_answer}")
    print("-" * 30)