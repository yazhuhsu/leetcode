package main

import (
	"fmt"
	"math"
	"strconv"
)

func mirrorDistance(n int) int {
	copy, mirror := n, 0
	for i := 1; i < len(strconv.Itoa(n))+1; i++ {
		mirror += (copy % 10) * int(math.Pow(10, float64(len(strconv.Itoa(n))-i)))
		copy /= 10
	}

	if mirror > n {
		return mirror - n
	}

	return n - mirror
}

func main() {
	// Walkthrough example
	fmt.Println(mirrorDistance(1234) == 3087)
	// Palindrome: mirror equals n
	fmt.Println(mirrorDistance(1221) == 0)
	// Leading zeros dropped in mirror: 100 → 001 = 1
	fmt.Println(mirrorDistance(100) == 99)
	// Single digit: mirror equals itself
	fmt.Println(mirrorDistance(7) == 0)
	// Mirror is larger than n
	fmt.Println(mirrorDistance(123) == 198)
}
