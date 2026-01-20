package main

import (
	"fmt"
	"reflect"
)

func minBitwiseArray(nums []int) []int {
	answers := make([]int, 0, len(nums))
	for idx, num := range nums {
		for i := 1; i <= num; i++ {
			if (i | (i + 1)) == num {
				answers = append(answers, i)
				break
			}
		}

		if len(answers) != idx+1 {
			answers = append(answers, -1)
		}
	}

	return answers
}

func main() {
	fmt.Println(reflect.DeepEqual(minBitwiseArray([]int{2, 3, 5, 7}), []int{-1, 1, 4, 3}))
	fmt.Println(reflect.DeepEqual(minBitwiseArray([]int{11, 13, 31}), []int{9, 12, 15}))
	fmt.Println(reflect.DeepEqual(minBitwiseArray([]int{149, 521, 71, 967, 449, 101, 439, 557, 73, 179}), []int{148, 520, 67, 963, 448, 100, 435, 556, 72, 177}))
}
