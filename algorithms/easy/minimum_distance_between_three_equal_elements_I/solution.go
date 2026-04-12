package main

import "fmt"

func minimumDistance(nums []int) int {
	goods := make(map[int][]int, 0)
	for idx, num := range nums {
		if _, ok := goods[num]; !ok {
			goods[num] = make([]int, 0)
		}

		goods[num] = append(goods[num], idx)
	}

	distance := -1
	for _, values := range goods {
		if len(values) < 3 {
			continue
		}

		for idx := 0; idx < len(values)-2; idx++ {
			d := (values[idx+1] - values[idx]) + (values[idx+2] - values[idx+1]) + (values[idx+2] - values[idx])

			if distance != -1 && d > distance {
				continue
			}

			distance = d
		}
	}

	return distance
}

func main() {
	// Walkthrough example: two qualifying values, value 2 wins
	fmt.Println(minimumDistance([]int{1, 2, 1, 2, 2, 1}) == 6)
	// Value 1 has 4 occurrences, best window [2,5,6] gives 8; value 2 still wins with 6
	fmt.Println(minimumDistance([]int{1, 2, 1, 2, 2, 1, 1}) == 6)
	// Only one qualifying value
	fmt.Println(minimumDistance([]int{1, 2, 1, 3, 1}) == 8)
	// No value appears 3 times
	fmt.Println(minimumDistance([]int{1, 2, 3}) == -1)
	// All same value, best window is first three
	fmt.Println(minimumDistance([]int{1, 1, 1, 1}) == 4)
	// Edge case: minimum possible distance (three consecutive equal elements)
	fmt.Println(minimumDistance([]int{5, 5, 5}) == 4)
}
