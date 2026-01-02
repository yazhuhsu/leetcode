package main

import (
	"fmt"
	"reflect"
)

func findErrorNums(nums []int) []int {
	numMap := make(map[int]int, len(nums))
	for _, num := range nums {
		numMap[num] += 1
	}

	dup, mis := 0, 0
	for i := 1; i < len(nums)+1; i++ {
		num, ok := numMap[i]
		if !ok {
			mis = i
		}
		if num > 1 {
			dup = i
		}
	}

	return []int{dup, mis}
}

func main() {
	fmt.Println(reflect.DeepEqual(findErrorNums([]int{1, 2, 2, 4}), []int{2, 3}))
	fmt.Println(reflect.DeepEqual(findErrorNums([]int{1, 1}), []int{1, 2}))
}
