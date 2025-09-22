package main

import "fmt"

func maxFrequencyElements(nums []int) int {
	frequencies, m := map[int]int{}, 0
	for _, n := range nums {
		frequencies[n] += 1

		if frequencies[n] > m {
			m = frequencies[n]
		}
	}

	count := 0
	for _, v := range frequencies {
		if v == m {
			count += 1
		}
	}

	return count * m
}

func main() {
	fmt.Println(maxFrequencyElements([]int{1, 2, 2, 3, 1, 4}) == 4)
	fmt.Println(maxFrequencyElements([]int{1, 2, 3, 4, 5}) == 5)
}
