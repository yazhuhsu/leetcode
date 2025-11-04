package main

import (
	"fmt"
	"reflect"
	"sort"
)

type Number struct {
	Num   int
	Count int
}

func findXSum(nums []int, k int, x int) []int {
	sums := make([]int, 0, len(nums)-k+1)
	for idx := 0; idx < len(nums)-k+1; idx++ {
		subNums := nums[idx : idx+k]
		countMap := make(map[int]int, len(subNums))
		for _, subNum := range subNums {
			countMap[subNum] += 1
		}

		counts := make([]Number, 0, len(countMap))
		for num, count := range countMap {
			counts = append(counts, Number{Num: num, Count: count})
		}

		sort.Slice(counts, func(i, j int) bool {
			if counts[i].Count == counts[j].Count {
				return counts[i].Num > counts[j].Num
			}

			return counts[i].Count > counts[j].Count
		})

		sums = append(sums, 0)
		if len(counts) < x {
			for _, count := range counts {
				sums[idx] += count.Num * count.Count
			}
			continue
		}

		for xIdx := 0; xIdx < x; xIdx++ {
			sums[idx] += counts[xIdx].Num * counts[xIdx].Count
		}
	}

	return sums
}

func main() {
	fmt.Println(reflect.DeepEqual(findXSum([]int{1, 1, 2, 2, 3, 4, 2, 3}, 6, 2), []int{6, 10, 12}))
	fmt.Println(reflect.DeepEqual(findXSum([]int{3, 8, 7, 8, 7, 5}, 2, 2), []int{11, 15, 15, 15, 12}))
}
