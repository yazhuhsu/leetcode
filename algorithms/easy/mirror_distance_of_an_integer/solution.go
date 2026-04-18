package main

import "fmt"

func mirrorDistance(n int) int {
	// build mirror by shifting left and appending last digit of num each iteration
	num, mirror := n, 0
	for num > 0 {
		mirror = mirror*10 + num%10
		num /= 10
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
