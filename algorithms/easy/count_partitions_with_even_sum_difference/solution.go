package main

import "fmt"

func countPartitions(nums []int) int {
	even, sumUp := 0, sum(nums)
	for i := 0; i < len(nums)-1; i++ {
		left := sum(nums[0 : i+1])
		right := sumUp - left
		if (left-right)%2 == 0 {
			even += 1
		}
	}

	return even
}

func sum(nums []int) int {
	count := 0
	for i := 0; i < len(nums); i++ {
		count += nums[i]
	}

	return count
}

func main() {
	fmt.Println(countPartitions([]int{10, 10, 3, 7, 6}) == 4)
	fmt.Println(countPartitions([]int{1, 2, 2}) == 0)
	fmt.Println(countPartitions([]int{2, 4, 6, 8}) == 3)
}
