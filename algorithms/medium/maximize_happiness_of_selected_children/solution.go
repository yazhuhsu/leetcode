package main

import (
	"fmt"
	"sort"
)

func maximumHappinessSum(happiness []int, k int) int64 {
	sort.Slice(happiness, func(i, j int) bool {
		return happiness[i] > happiness[j]
	})

	maxSum := int64(0)
	for idx, value := range happiness[:k] {
		if value-idx < 0 {
			break
		}
		maxSum += int64(value) - int64(idx)
	}

	return maxSum
}

func main() {
	fmt.Println(maximumHappinessSum([]int{1, 2, 3}, 2) == 4)
	fmt.Println(maximumHappinessSum([]int{1, 1, 1, 1}, 2) == 1)
	fmt.Println(maximumHappinessSum([]int{2, 3, 4, 5}, 1) == 5)
}
