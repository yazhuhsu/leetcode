package main

import "fmt"

func countOdds(low int, high int) int {
	nums := 0
	if low%2 == 1 {
		nums += 1
		low += 1
	}
	if high%2 == 1 {
		nums += 1
		high -= 1
	}

	nums += (high - low) / 2

	return nums
}

func main() {
	fmt.Println(countOdds(3, 7) == 3)
	fmt.Println(countOdds(8, 10) == 1)
	fmt.Println(countOdds(0, 1000000000) == 500000000)
	fmt.Println(countOdds(21, 22) == 1)
}
