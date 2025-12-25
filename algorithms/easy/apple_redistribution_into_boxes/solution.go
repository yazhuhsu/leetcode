package main

import (
	"fmt"
	"sort"
)

func minimumBoxes(apple []int, capacity []int) int {
	sort.Slice(capacity, func(i, j int) bool {
		return capacity[i] > capacity[j]
	})

	sum := 0
	for _, a := range apple {
		sum += a
	}

	boxes := 0
	for _, cap := range capacity {
		if cap <= sum {
			sum = sum - cap
			boxes += 1
			continue
		}

		if sum > 0 {
			boxes += 1
		}
		break
	}

	return boxes
}

func main() {
	fmt.Println(minimumBoxes([]int{1, 3, 2}, []int{4, 3, 1, 5, 2}) == 2)
	fmt.Println(minimumBoxes([]int{5, 5, 5}, []int{2, 4, 2, 7}) == 4)
}
