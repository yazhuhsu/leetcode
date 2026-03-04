package main

import (
	"fmt"
	"reflect"
)

func sortArrayByParityII(nums []int) []int {
	odds, evens := make([]int, 0), make([]int, 0)
	for idx, num := range nums {
		if idx%2 == 0 && num%2 != 0 {
			odds = append(odds, idx)
			continue
		}

		if idx%2 != 0 && num%2 == 0 {
			evens = append(evens, idx)
			continue
		}
	}

	for i := 0; i < len(odds); i++ {
		odd, even := nums[odds[i]], nums[evens[i]]
		nums[odds[i]] = even
		nums[evens[i]] = odd
	}

	return nums
}

func main() {
	fmt.Println(reflect.DeepEqual(sortArrayByParityII([]int{4, 2, 5, 7}), []int{4, 5, 2, 7}))
	fmt.Println(reflect.DeepEqual(sortArrayByParityII([]int{2, 3}), []int{2, 3}))
}
