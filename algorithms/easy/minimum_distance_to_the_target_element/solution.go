package main

import "fmt"

func getMinDistance(nums []int, target int, start int) int {
	minimized := 1000 + start
	for idx, num := range nums {
		if num != target {
			continue
		}

		m := idx - start
		if idx < start {
			m = start - idx
		}
		if minimized > m {
			minimized = m
		}
	}

	return minimized
}

func main() {
	// Target appears on both sides of start, closer one wins
	fmt.Println(getMinDistance([]int{1, 2, 3, 4, 5}, 5, 3) == 1)
	// Target only appears before start
	fmt.Println(getMinDistance([]int{1, 2, 3, 4, 5}, 1, 4) == 4)
	// Target is at start index
	fmt.Println(getMinDistance([]int{1, 2, 3, 4, 5}, 3, 2) == 0)
	// Multiple occurrences of target, pick closest
	fmt.Println(getMinDistance([]int{1, 1, 1, 1, 1}, 1, 2) == 0)
	// Target at both ends, start in middle
	fmt.Println(getMinDistance([]int{5, 3, 6, 5}, 5, 2) == 1)
}
