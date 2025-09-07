package main

import "fmt"

func sumZero(n int) []int {
	outputs := make([]int, 0, n)
	if n%2 == 1 {
		outputs = append(outputs, 0)
		n -= 1
	}

	for i := 2; i < n+2; i++ {
		output := i / 2
		if i%2 == 1 {
			output = -output
		}
		outputs = append(outputs, output)
	}

	return outputs
}

func main() {
	answers := map[int][]int{
		5: {0, 1, -1, 2, -2},
		3: {0, 1, -1},
		1: {0},
	}

	for n, answer := range answers {
		existCount := 0
		for _, output := range sumZero(n) {
			for _, a := range answer {
				if output == a {
					existCount += 1
				}
			}
		}

		if existCount == n {
			fmt.Println(true)
		}
	}
}
