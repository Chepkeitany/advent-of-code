package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
)

func convertToInts(values[] string)([]int, error) {
	var numbers []int

	for _, str := range values {
		number, err := strconv.Atoi(str)

		if err != nil {
			return nil, err
		}

		numbers = append(numbers, number)
	}

	return numbers, nil
}

func evaluateExprLeftToRight(numbers []int, operators []string) int {
	result := numbers[0]
	for i := 0; i < len(operators); i++ {
		if operators[i] == "+" {
			result += numbers[i+1]
		} else if operators[i] == "*" {
			result *= numbers[i+1]
		} else if operators[i] == "||" {
			// Handle concatenation operator
			concatenated_value, _ := strconv.Atoi(strconv.Itoa(result) + strconv.Itoa(numbers[i + 1]))
			result = concatenated_value
		}
	}
	return result
}

func generateCombinations(operators []string, n int) [][]string {
	if n == 0 {
		return [][]string{{}}
	}

	// Recursive generation of combinations
	subCombinations := generateCombinations(operators, n-1)
	var combinations [][]string
	for _, sub := range subCombinations {
		for _, op := range operators {
			combo := append([]string{op}, sub...)
			combinations = append(combinations, combo)
		}
	}
	return combinations
} 

func findTargetResult(numbers []int, operators[]string, target int) bool {
	n := len(numbers)

	if n == 0 {
		return false
	}

	if n == 1 {
		return numbers[0] == target
	}

	// Generate all combinations of operators
	operatorCombinations := generateCombinations(operators, n - 1)

	for _, operatorCombination := range operatorCombinations {
		result := evaluateExprLeftToRight(numbers, operatorCombination)

		if result == target {
			return true
		}
	}

	return false
}

func main() {
	file, err := os.Open("day7_all.txt")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close() // Ensure the file is closed when the function ends

	// Initialize total calibration result
	totalCalibrationResult := 0
	// Read the file line by line
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.TrimSpace(scanner.Text())

		parts := strings.Split(line, ": ")
		result, err := strconv.Atoi(parts[0])
		values := strings.Split(parts[1], " ")

		// Convert the numbers to integers
		numbers, err := convertToInts(values)
		if err != nil {
			fmt.Println("Error! The input does not contain all ints")
		}

		// fmt.Println(result)
		// fmt.Println(numbers)

		// Add to the calibration result if we can find the possible_result by
		// trying all the combinations of expressions by using the given operators
		// and evaluating the expression from left to right (not by order of precedence)

		// Introduce the || concatenation operator
		operators := []string{"+", "*", "||"}

		if findTargetResult(numbers, operators, result) {
			totalCalibrationResult += result
		}

	}

	fmt.Println(totalCalibrationResult)
}
