package main

import "fmt"

func countNegatives(grid [][]int) int {
	count := 0
	for i := 0; i < len(grid); i++ {
		for j := len(grid[0]) - 1; j >= 0; j-- {
			if grid[i][j] >= 0 {
				break
			}

			count += 1
		}
	}

	return count
}

func main() {
	fmt.Println(countNegatives([][]int{{4, 3, 2, -1}, {3, 2, 1, -1}, {1, 1, -1, -2}, {-1, -1, -2, -3}}) == 8)
	fmt.Println(countNegatives([][]int{{3, 2}, {1, 0}}) == 0)
}
