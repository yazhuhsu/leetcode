package main

import "fmt"

func isTrionic(nums []int) bool {
	p, q, n := 0, 0, len(nums)-1
	for idx, num := range nums {
		if idx == 0 {
			continue
		}
		if num < nums[idx-1] && p == 0 {
			p = idx - 1
		}
		if num > nums[idx-1] && p != 0 && q == 0 {
			q = idx - 1
			break
		}
	}

	if p == 0 || q == 0 {
		return false
	}

	for i := 1; i <= p; i++ {
		if nums[i] <= nums[i-1] {
			return false
		}
	}

	for i := p + 1; i <= q; i++ {
		if nums[i] >= nums[i-1] {
			return false
		}
	}

	for i := q + 1; i <= n; i++ {
		if nums[i] <= nums[i-1] {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(isTrionic([]int{1, 3, 5, 4, 2, 6}) == true)
	fmt.Println(isTrionic([]int{2, 1, 3}) == false)
	fmt.Println(isTrionic([]int{8, 8, 2, 6}) == false)
}
