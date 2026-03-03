package main

import "fmt"

func dominantIndex(nums []int) int {
	max, maxIdx, second := -1, -1, -1
	for idx, num := range nums {
		if max == -1 {
			max, maxIdx = num, idx
			continue
		}

		if num > max {
			second = max
			max, maxIdx = num, idx
			continue
		}

		if num > second {
			second = num
		}
	}

	if max >= second*2 {
		return maxIdx
	}

	return -1
}

func main() {
	fmt.Println(dominantIndex([]int{3, 6, 1, 0}) == 1)
	fmt.Println(dominantIndex([]int{1, 2, 3, 4}) == -1)
}
