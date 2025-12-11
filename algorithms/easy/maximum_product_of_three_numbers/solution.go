package main

import (
	"fmt"
	"sort"
)

func maximumProduct(nums []int) int {
	if len(nums) == 3 {
		return nums[0] * nums[1] * nums[2]
	}
	sort.Slice(nums, func(i, j int) bool { return nums[i] < nums[j] })

	counts := make([]int, 0, 3)
	for _, num := range nums[:3] {
		if num > 0 {
			break
		}
		counts = append(counts, num)
	}

	min, max := 0, nums[len(nums)-3]*nums[len(nums)-2]*nums[len(nums)-1]
	if len(counts) >= 2 {
		min = counts[0] * counts[1] * nums[len(nums)-1]
	}
	if min > max {
		return min
	} else {
		return max
	}
}

func main() {
	fmt.Println(maximumProduct([]int{1, 2, 3}) == 6)
	fmt.Println(maximumProduct([]int{1, 2, 3, 4}) == 24)
	fmt.Println(maximumProduct([]int{-1, -2, -3}) == -6)
	fmt.Println(maximumProduct([]int{-34, 1, 2, 3, 4, 5}) == 60)
	fmt.Println(maximumProduct([]int{-34, -33, 2, 3, 4, 5}) == 5610)
	fmt.Println(maximumProduct([]int{-100, -98, -1, 2, 3, 4}) == 39200)
	fmt.Println(maximumProduct([]int{-100, -2, -3, 1}) == 300)
}
