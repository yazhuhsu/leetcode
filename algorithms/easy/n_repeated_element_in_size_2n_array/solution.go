package main

import "fmt"

func repeatedNTimes(nums []int) int {
	numMap := make(map[int]bool, len(nums))
	for _, num := range nums {
		if numMap[num] {
			return num
		}

		numMap[num] = true
	}

	return 0
}

func main() {
	fmt.Println(repeatedNTimes([]int{1, 2, 3, 3}) == 3)
	fmt.Println(repeatedNTimes([]int{2, 1, 2, 5, 3, 2}) == 2)
	fmt.Println(repeatedNTimes([]int{5, 1, 5, 2, 5, 3, 5, 4}) == 5)
}
