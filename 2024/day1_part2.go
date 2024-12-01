package main

// go run day1_part2.go with the day1_all.txt file in the same directory

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("day1_all.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close() // Ensure the file is closed when the function ends

	var leftList, rightList []int

	// Read the file line by line
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())

		// Remember the input is separated by double spaces
		parts := strings.Split(line, "  ")
		if len(parts) != 2 {
			fmt.Println("Invalid line format:", line)
			continue
		}

		// Convert to numbers
		leftNum, err1 := strconv.Atoi(strings.TrimSpace(parts[0]))
		rightNum, err2 := strconv.Atoi(strings.TrimSpace(parts[1]))
		if err1 != nil || err2 != nil {
			fmt.Println("Error converting to integer:", parts)
			continue
		}

		leftList = append(leftList, leftNum)
		rightList = append(rightList, rightNum)
	}

	// Check for errors during scanning
	if err := scanner.Err(); err != nil {
		fmt.Println("Error reading file:", err)
	}


	// Build a frequency map of the right slice
	rightListfrequencyMap := make(map[int]int)

	for _, num := range rightList {
		rightListfrequencyMap[num]++
	}

	// Calculate the total similarity score
	totalSimilarityScore := 0
	for _, num := range leftList {
		if count, exists := rightListfrequencyMap[num]; exists {
			totalSimilarityScore += num * count
		}
	}

	fmt.Println("Total Similarity Score:", totalSimilarityScore)
}