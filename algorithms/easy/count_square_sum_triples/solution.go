package main

import (
	"fmt"
	"math"
)

func countTriples(n int) int {
	triples := make([][]int, 0)
	for i := n; i > 0; i-- {
		for j := i - 1; j > 0; j-- {
			k := math.Sqrt(float64(i*i - j*j))
			if float64(int(k)) == k && int(k) < i {
				triples = append(triples, []int{j, int(k), i})
			}
		}
	}

	return len(triples)
}

func main() {
	fmt.Println(countTriples(5) == 2)
	fmt.Println(countTriples(10) == 4)
}
