package main

import (
	"fmt"
	"reflect"
)

func nextGreaterElement(nums1 []int, nums2 []int) []int {
	find, ans := false, make([]int, 0, len(nums1))
	for idx, num1 := range nums1 {
		find = false
		for _, num2 := range nums2 {
			if num1 == num2 {
				find = true
				continue
			}

			if find && num2 > num1 {
				ans = append(ans, num2)
				break
			}
		}

		if len(ans) != idx+1 {
			ans = append(ans, -1)
		}
	}

	return ans
}

func main() {
	fmt.Println(reflect.DeepEqual(nextGreaterElement([]int{4, 1, 2}, []int{1, 3, 4, 2}), []int{-1, 3, -1}))
	fmt.Println(reflect.DeepEqual(nextGreaterElement([]int{2, 4}, []int{1, 2, 3, 4}), []int{3, -1}))
}
