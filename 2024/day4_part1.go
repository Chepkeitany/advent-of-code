package main

import (
	"fmt"
	"image"
	"os"
	"strings"
)

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
	file, _ := os.ReadFile("day4_all.txt")

	rows := strings.Split(strings.TrimSpace(string(file)), "\n")

	// Initialize an empty map where key is the Point(x,y) coordinate and value is the character at that position
	grid := map[image.Point]rune{}
	for rowIndex, row :=  range rows {
		for colIndex, value := range row {
			grid[image.Point{rowIndex, colIndex}] = value
		}
	}

	// Find the total occurrences of the word XMAS
	totalOccurrences := 0

	wordLen := 4 // XMAS is a 4-letter word so we want to generate words of length 4 at a time
	for point := range grid {
		totalOccurrences += strings.Count(strings.Join(generateWords(point, wordLen, grid), " "), "XMAS")
	}

	fmt.Println(totalOccurrences)
}