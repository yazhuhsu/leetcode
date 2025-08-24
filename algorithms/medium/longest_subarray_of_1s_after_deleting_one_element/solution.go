package main

import "fmt"

func longestSubarray(nums []int) int {
	zeros := make([]int, 0)
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			zeros = append(zeros, i)
		}
	}

	if len(zeros) == 0 {
		return len(nums) - 1
	}

	max := 0
	for z := 0; z < len(zeros); z++ {
		start, end := 0, len(nums)-1
		if z != 0 {
			start = zeros[z-1] + 1
		}
		if z != len(zeros)-1 {
			end = zeros[z+1] - 1
		}

		if end-start > max {
			max = end - start
		}
	}

	return max
}

func main() {
	fmt.Println(longestSubarray([]int{1, 1, 0, 1}) == 3)
	fmt.Println(longestSubarray([]int{0, 1, 1, 1, 0, 1, 1, 0, 1}) == 5)
	fmt.Println(longestSubarray([]int{1, 1, 1}) == 2)
}
