package main

import "fmt"

func findMaxConsecutiveOnes(nums []int) int {
	count, maxCount := 0, 0
	for i := 0; i < len(nums); i++ {
		if nums[i] == 1 {
			count += 1
		} else {
			if maxCount < count {
				maxCount = count
			}
			count = 0
		}

		if i == len(nums)-1 {
			if maxCount < count {
				maxCount = count
			}
		}
	}

	return maxCount
}

func main() {
	fmt.Println(findMaxConsecutiveOnes([]int{1, 1, 0, 1, 1, 1}) == 3)
	fmt.Println(findMaxConsecutiveOnes([]int{1, 0, 1, 1, 0, 1}) == 2)
}
