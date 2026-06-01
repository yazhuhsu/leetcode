package main

import (
	"fmt"
	"sort"
)

func minimumCost(cost []int) int {
	sort.Slice(cost, func(i, j int) bool {
		return cost[i] > cost[j]
	})

	costs, bought := 0, 0
	for _, c := range cost {
		if bought == 2 {
			bought = 0
			continue
		}
		costs += c
		bought += 1
	}

	return costs
}

func main() {
	fmt.Println(minimumCost([]int{1, 2, 3}) == 5)
	fmt.Println(minimumCost([]int{6, 5, 7, 9, 2, 2}) == 23)
	fmt.Println(minimumCost([]int{5, 5}) == 10)
	fmt.Println(minimumCost([]int{1}) == 1)
	fmt.Println(minimumCost([]int{3, 3, 3}) == 6)
}
