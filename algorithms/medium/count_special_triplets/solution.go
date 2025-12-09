package main

import (
	"fmt"
	"math"
)

func specialTriplets(nums []int) int {
	mod := int(math.Pow(10, 9) + 7)
	numMap := make(map[int][]int)

	for idx, num := range nums {
		if _, ok := numMap[num]; !ok {
			numMap[num] = make([]int, 0)
		}
		numMap[num] = append(numMap[num], idx)
	}

	if len(numMap) == 1 {
		if len(numMap[0]) > 0 {
			count := (len(nums) - 2) * (len(nums) - 1) * len(nums) / 6
			return count % mod
		} else {
			return 0
		}
	}

	count := 0
	for key, value := range numMap {
		twice := key * 2
		twiceNums, ok := numMap[twice]
		if !ok {
			continue
		}

		for _, v := range value {
			idx := binarySearch(twiceNums, v)
			if key == twice {
				count += (idx - 1) * (len(twiceNums) - idx)
			} else {
				count += idx * (len(twiceNums) - idx)
			}
		}
	}

	return count % mod
}

func binarySearch(numbers []int, key int) int {
	start, end := 0, len(numbers)-1
	for start <= end {
		mid := (start + end) / 2

		if numbers[mid] > key {
			end = mid - 1
		} else {
			start = mid + 1
		}
	}

	return start
}

func main() {
	fmt.Println(specialTriplets([]int{6, 3, 6}) == 1)
	fmt.Println(specialTriplets([]int{0, 1, 0, 0}) == 1)
	fmt.Println(specialTriplets([]int{8, 4, 2, 8, 4}) == 2)
}
