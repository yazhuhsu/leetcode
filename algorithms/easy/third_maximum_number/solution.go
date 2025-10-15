package main

import (
	"fmt"
	"math"
)

func thirdMax(nums []int) int {
	numMap := make(map[int]bool, len(nums))
	for _, num := range nums {
		if !numMap[num] {
			numMap[num] = true
		}
	}

	first, second, third := math.MinInt32-1, math.MinInt32-1, math.MinInt32-1
	for num := range numMap {
		if num > first {
			if second != math.MinInt32-1 {
				third = second
			}
			if first != math.MinInt32-1 {
				second = first
			}
			first = num
		} else if num > second {
			if second != math.MinInt32-1 {
				third = second
			}
			second = num
		} else if num > third {
			third = num
		}
	}

	if third == math.MinInt32-1 {
		return first
	}

	return third
}

func main() {
	fmt.Println(thirdMax([]int{3, 2, 1}) == 1)
	fmt.Println(thirdMax([]int{1, 2}) == 2)
	fmt.Println(thirdMax([]int{2, 2, 3, 1}) == 1)
}
