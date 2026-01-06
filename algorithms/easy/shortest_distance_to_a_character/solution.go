package main

import (
	"fmt"
	"math"
	"reflect"
)

func shortestToChar(s string, c byte) []int {
	indices := make([]int, 0, len(s))
	for idx, r := range s {
		if r == rune(c) {
			indices = append(indices, idx)
		}
	}

	distances := make([]int, 0, len(s))
	for idx, _ := range s {
		distance := len(s)
		for _, ind := range indices {
			if int(math.Abs(float64(idx)-float64(ind))) < distance {
				distance = int(math.Abs(float64(idx) - float64(ind)))
			}
		}
		distances = append(distances, distance)
	}

	return distances
}

func main() {
	fmt.Println(reflect.DeepEqual(shortestToChar("loveleetcode", 'e'), []int{3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0}))
	fmt.Println(reflect.DeepEqual(shortestToChar("aaab", 'b'), []int{3, 2, 1, 0}))
}
