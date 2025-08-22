package main

import "fmt"

func minimumArea(grid [][]int) int {
	top, down, left, right := -1, -1, -1, -1
	for row := 0; row < len(grid); row++ {
		for column := 0; column < len(grid[0]); column++ {
			if top == -1 && grid[row][column] == 1 {
				top = row
			}

			if down == -1 && grid[len(grid)-row-1][len(grid[0])-column-1] == 1 {
				down = len(grid) - row - 1
			}
		}
	}

	for column := 0; column < len(grid[0]); column++ {
		for row := 0; row < len(grid); row++ {
			if left == -1 && grid[row][column] == 1 {
				left = column
			}

			if right == -1 && grid[len(grid)-row-1][len(grid[0])-column-1] == 1 {
				right = len(grid[0]) - column - 1
			}
		}
	}

	w, h := right-left+1, down-top+1

	return w * h
}

func main() {
	fmt.Println(minimumArea([][]int{
		{0, 1, 0},
		{1, 0, 1},
	}) == 6)

	fmt.Println(minimumArea([][]int{
		{1, 0},
		{0, 0},
	}) == 1)
}
