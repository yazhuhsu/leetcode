package main

import (
	"fmt"
	"reflect"
	"slices"
)

func minimumAbsDifference(arr []int) [][]int {
	slices.Sort(arr[:])

	mini, differences := -1, make([][]int, 0)
	for idx := 0; idx < len(arr)-1; idx++ {
		abs := arr[idx+1] - arr[idx]
		if mini == -1 || abs < mini {
			mini = abs
		}
	}

	for idx := 0; idx < len(arr)-1; idx++ {
		abs := arr[idx+1] - arr[idx]
		if abs == mini {
			differences = append(differences, []int{arr[idx], arr[idx+1]})
		}
	}

	return differences
}

func main() {
	fmt.Println(reflect.DeepEqual(minimumAbsDifference([]int{4, 2, 1, 3}), [][]int{{1, 2}, {2, 3}, {3, 4}}))
	fmt.Println(reflect.DeepEqual(minimumAbsDifference([]int{1, 3, 6, 10, 15}), [][]int{{1, 3}}))
	fmt.Println(reflect.DeepEqual(minimumAbsDifference([]int{3, 8, -10, 23, 19, -4, -14, 27}), [][]int{{-14, -10}, {19, 23}, {23, 27}}))
}
