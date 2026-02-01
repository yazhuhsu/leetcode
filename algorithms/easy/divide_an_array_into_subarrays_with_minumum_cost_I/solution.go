package main

import (
	"fmt"
	"sort"
)

func minimumCost(nums []int) int {
	sort.Ints(nums[1:])

	return nums[0] + nums[1] + nums[2]
}

func main() {
	fmt.Println(minimumCost([]int{1, 2, 3, 12}) == 6)
	fmt.Println(minimumCost([]int{10, 3, 1, 1}) == 12)
	fmt.Println(minimumCost([]int{5, 4, 3}) == 12)
}
