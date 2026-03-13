package main

import (
	"fmt"
	"reflect"
)

func smallerNumbersThanCurrent(nums []int) []int {
	numMap := make(map[int]int, len(nums))
	for _, num := range nums {
		numMap[num] += 1
	}

	counts := make([]int, 0, len(nums))
	for idx, num := range nums {
		counts = append(counts, 0)
		for k, v := range numMap {
			if k < num {
				counts[idx] += v
			}
		}
	}

	return counts
}

func main() {
	fmt.Println(reflect.DeepEqual(smallerNumbersThanCurrent([]int{8, 1, 2, 2, 3}), []int{4, 0, 1, 1, 3}))
	fmt.Println(reflect.DeepEqual(smallerNumbersThanCurrent([]int{6, 5, 4, 8}), []int{2, 1, 0, 3}))
	fmt.Println(reflect.DeepEqual(smallerNumbersThanCurrent([]int{7, 7, 7, 7}), []int{0, 0, 0, 0}))
}
