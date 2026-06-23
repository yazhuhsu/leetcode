package main

import (
	"fmt"
	"math"
)

func numberOfWays(n int, x int) int {
	possibleNums := []int{}
	for i := 1; i <= n+1; i++ {
		if math.Pow(float64(i), float64(x)) > float64(n) {
			break
		}

		possibleNums = append(possibleNums, i)
	}

	count := 0
	for i := 1; i < len(possibleNums)+1; i++ {
		possibleCombinations := calculateCombinations(possibleNums, i)

		for _, possibleCombination := range possibleCombinations {
			sum := float64(0)
			for _, a := range possibleCombination {
				sum += math.Pow(float64(a), float64(x))
			}

			if sum == float64(n) {
				count += 1
			}
		}
	}

	return count
}

func calculateCombinations(nums []int, num int) (combinations [][]int) {
	var generate func(startIdx int, added []int, nums []int, num int, combinations *[][]int)
	generate = func(startIdx int, added []int, nums []int, num int, combinations *[][]int) {
		if len(added) == num {
			combination := make([]int, len(added))
			copy(combination, added)
			*combinations = append(*combinations, combination)
			return
		}

		for idx := startIdx; idx < len(nums); idx++ {
			added = append(added, nums[idx])
			generate(idx+1, added, nums, num, combinations)
			added = added[:len(added)-1]
		}
	}

	generate(0, []int{}, nums, num, &combinations)

	return
}

func main() {
	fmt.Println(numberOfWays(10, 2))
	fmt.Println(numberOfWays(1, 1))
	fmt.Println(numberOfWays(22, 1))
}
