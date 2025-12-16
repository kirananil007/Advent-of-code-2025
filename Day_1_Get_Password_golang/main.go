package main

import (
	"fmt"
	"os"
	"net/http"
	"io"
	"strconv"
	"strings"
)

const session_cookie = "53616c7465645f5f257629c68340882a2f4c9317038ad7f407056d54347ba68f01d68f96295d4e2e01cedc40620aa58d796a708084a85ec680e433c996b3c924"
const year = 2025
const filename = "input.txt"
const day = 1


func getAoCInput(day int, cookie string) (string, error) {
	// Check Local
	if _, err := os.Stat(filename); err == nil {
		fmt.Printf("Reading local file: %s\n", filename)
		content, err := os.ReadFile(filename)
		return string(content), err
	}
	fmt.Printf("Downloading input for Day %d...\n", day)
	url := fmt.Sprintf("https://adventofcode.com/%d/day/%d/input", year, day)

	req, _ := http.NewRequest("GET", url, nil)
	req.Header.Set("Cookie", "session="+cookie)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return "", err
	}

	defer resp.Body.Close()

	if resp.StatusCode != 200 {
		return "", fmt.Errorf("API returned status %d", resp.StatusCode)
	}

	body, _ := io.ReadAll(resp.Body)
	
	// Save to local
	os.WriteFile(filename, body, 0644)
	
	return string(body), nil
}


func solvePart1(lines []string) int {
	currentPos := 50
	zeroHits := 0

	for _, line := range lines {
		if line == "" {
			continue
		}

		direction := line[0]             // Get R or L
		distance, _ := strconv.Atoi(line[1:]) // Convert to Int

		if direction == 'R' {
			currentPos = (currentPos + distance) % 100
		} else if direction == 'L' {
			currentPos = (currentPos - distance) % 100
			if currentPos < 0 {
				currentPos += 100
			}
		}

		if currentPos == 0 {
			zeroHits++
		}
	}
	return zeroHits
}

func main() {
    fmt.Println("Hello, World!")
	getAoCInput(1, session_cookie)	
	data, err := getAoCInput(day, session_cookie)
	if err != nil {
		fmt.Printf("Error getting input: %v\n", err)
		return
	}

	lines := strings.Split(strings.TrimSpace(data), "\n")


	fmt.Println("--- Advent of Code 2025 Day 1 ---")
	fmt.Println("This is the input data: %d\n", data)
	fmt.Printf("Part 1 --> Answer: %d\n", solvePart1(lines))
}
