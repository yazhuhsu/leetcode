package main

import (
	"fmt"
	"reflect"
	"strconv"
	"strings"
)

func selfDividingNumbers(left int, right int) []int {
	nums := make([]int, 0, right-left+1)
	for i := left; i <= right; i++ {
		if isDivided(i) {
			nums = append(nums, i)
		}
	}

	return nums
}

func isDivided(num int) bool {
	numMap := make(map[int]bool, len(string(num)))
	strs := strconv.Itoa(num)
	for _, str := range strings.Split(strs, "") {
		r, _ := strconv.Atoi(str)
		numMap[r] = true
	}

	for n, _ := range numMap {
		if n == 0 {
			return false
		}
		if num%n != 0 {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(reflect.DeepEqual(selfDividingNumbers(1, 22), []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22}))
	fmt.Println(reflect.DeepEqual(selfDividingNumbers(47, 85), []int{48, 55, 66, 77}))
}
