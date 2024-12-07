package main

import (
	"fmt"
	"os"
	"strings"
	"sort"
	"strconv"
)

func compareRules(x, y string, rulesMap map[string]bool) bool {
	return rulesMap[x+"|"+y]
}

func main() {
	// Read input from the file
	file, _ := os.ReadFile("day5_all.txt")

	content := strings.Split(strings.TrimSpace(string(file)), "\n\n")

	rules := strings.Split(content[0], "\n")
	pages := strings.Split(content[1], "\n")

	// fmt.Println(rules)
	// fmt.Println(pages)

	rulesMap := make(map[string]bool)
	for _, rule := range rules {
		rulesMap[rule] = true
	}

	sumOfMiddlePageNumbers := 0

	// Process each page
	for _, page := range pages {
		parts := strings.Split(page, ",")
		original := append([]string(nil), parts...) // Copy for comparison

		// We want to try and sort the page numbers 
		sort.Slice(parts, func(i, j int) bool {
			return compareRules(parts[i], parts[j], rulesMap)
		})

		// Check if sorting changed the order
		changed := false
		for i := range original {
			if original[i] != parts[i] {
				changed = true
				break
			}
		}

		// Find the middle value
		middleValue, _ := strconv.Atoi(parts[len(parts)/2])

		// Update the results array
		if changed {
			continue
		} else {
			sumOfMiddlePageNumbers += middleValue
		}
	}

	fmt.Println(sumOfMiddlePageNumbers)
}
