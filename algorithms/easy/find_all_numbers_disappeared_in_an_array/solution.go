package main

import (
	"fmt"
	"reflect"
)

func findDisappearedNumbers(nums []int) []int {
	numMap := make(map[int]bool, len(nums))
	for _, num := range nums {
		if !numMap[num] {
			numMap[num] = true
		}
	}

	disappeared := make([]int, 0, len(nums))
	for i := 1; i < len(nums)+1; i++ {
		if !numMap[i] {
			disappeared = append(disappeared, i)
		}
	}

	return disappeared
}

func main() {
	fmt.Println(reflect.DeepEqual(findDisappearedNumbers([]int{4, 3, 2, 7, 8, 2, 3, 1}), []int{5, 6}))
	fmt.Println(reflect.DeepEqual(findDisappearedNumbers([]int{1, 1}), []int{2}))
}
