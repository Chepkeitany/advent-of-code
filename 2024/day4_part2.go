package main

import (
	"fmt"
	"image"
	"os"
	"strings"
)

func countXMasPatterns(grid map[image.Point]rune) int {
	totalOccurrences := 0

	// Iterate through all points in the grid
	for p := range grid {
		// Generate the words in 8 directions (2 steps long)
		words := generateWords(p, 2, grid)

		fmt.Printf("Point %v generated words: %v\n", p, words)


		// Look at the diagonal directions (index 4, 5, 6, 7)
		diagonalWords := words[4:] // Diagonals (Top-left, Top-right, Bottom-left, Bottom-right)

		// Join the diagonal words into a single string
		joinedDiagonals := strings.Join(diagonalWords, "")

		// Check if the X-MAS pattern (M.S.A.M.S) appears in the joined diagonal string
		if strings.Count(joinedDiagonals, "AMAMASASAMAMAS") > 0 {
			totalOccurrences++
		}
	}

	return totalOccurrences
}

// func countXMasPatterns(grid map[image.Point]rune) int {
// 	totalOccurrences := 0

// 	for p := range grid {
// 		// Generate words from the current point
// 		words := generateWords(p, 5, grid)
// 		fmt.Printf("Point %v generated words: %v\n", p, words)

// 		// Combine diagonals into a single string
// 		diagonalWords := strings.Join(words[4:], "") // Indices 4-7 are diagonals
// 		fmt.Printf("Point %v diagonal words: %s\n", p, diagonalWords)

// 		// Check for patterns in the diagonals
// 		count := strings.Count(diagonalWords, "AMAS")
// 		fmt.Printf("Point %v has %d occurrences of 'AMAS'\n", p, count)
// 		totalOccurrences += count
// 	}

// 	return totalOccurrences
// }

// generateWords generates words by moving in 8 directions from a point.
func generateWords(p image.Point, l int, grid map[image.Point]rune) []string {
	// Directions to move in 8 possible ways (N, E, S, W, and diagonals).
	directions := []image.Point{
		{0, -1}, {1, 0}, {0, 1}, {-1, 0}, // Up, Right, Down, Left
		{-1, -1}, {1, -1}, {1, 1}, {-1, 1}, // Diagonals (Top-left, Top-right, Bottom-right, Bottom-left)
	}

	// Initialize a slice to hold the words
	words := make([]string, len(directions))

	// Loop through each direction and create the words
	for i, dir := range directions {
		var word string
		for n := 0; n < l; n++ {
			// Move in the direction and append the character from the grid
			newPoint := p.Add(Mul(dir, n))
			word += string(grid[newPoint])
		}
		words[i] = word
	}

	return words
}

// Helper function to multiply a point by a scalar (for scaling direction).
func Mul(point image.Point, n int) image.Point {
	return image.Point{point.X * n, point.Y * n}
}

func main() {
	// Read input from the file
	file, _ := os.ReadFile("day4_all.txt")

	rows := strings.Split(strings.TrimSpace(string(file)), "\n")

	// Initialize an empty map where key is the Point(x,y) coordinate and value is the character at that position
	grid := map[image.Point]rune{}
	// Populate the grid with input from the file
	for rowIndex, row :=  range rows {
		for colIndex, value := range row {
			grid[image.Point{rowIndex, colIndex}] = value
		}
	}

	// Find the total occurrences X-MAS
	totalOccurrences := 0

	// wordLen := 4 // XMAS is a 4-letter word so we want to generate words of length 4 at a time
	for point := range grid {
		// Generate the words in 8 directions (2 steps long)
		words := generateWords(point, 2, grid)


		// Look at the diagonal directions (index 4, 5, 6, 7)
		diagonalWords := words[4:] // Diagonals (Top-left, Top-right, Bottom-left, Bottom-right)

		// Join the diagonal words into a single string
		joinedDiagonals := strings.Join(diagonalWords, "")

		// Check if the X-MAS pattern appears in the joined diagonal string
		if strings.Count("AMAMASASAMAMAS", joinedDiagonals) > 0 {
			totalOccurrences += 1
		}
	}

	fmt.Println(totalOccurrences)
}