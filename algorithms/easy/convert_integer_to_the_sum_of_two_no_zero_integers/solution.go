package main

import (
	"fmt"
	"slices"
	"strconv"
	"strings"
)

func getNoZeroIntegers(n int) []int {
	outputs := make([]int, 0, 2)
	for i := 1; i <= n; i++ {
		if strings.Contains(strconv.Itoa(i), "0") || strings.Contains(strconv.Itoa(n-i), "0") {
			continue
		}

		outputs = append(outputs, i)
		outputs = append(outputs, n-i)
		break
	}

	return outputs
}

func main() {
	answers := map[int][]int{
		2:  {1, 1},
		11: {2, 9},
	}

	for n, answer := range answers {
		existCount := 0
		for _, output := range getNoZeroIntegers(n) {
			if slices.Contains(answer, output) {
				existCount += 1
			}
		}

		if existCount == 2 {
			fmt.Println(true)
		}
	}
}
