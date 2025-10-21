package main

import (
	"fmt"
	"math"
)

func arrangeCoins(n int) int {
	s := 0
	for i := 1; i < math.MaxInt32; i++ {
		if n == s+i {
			return i
		} else if n > s && n < s+i {
			return i - 1
		}
		s += i
	}

	return 0
}

func main() {
	fmt.Println(arrangeCoins(5) == 2)
	fmt.Println(arrangeCoins(8) == 3)
}
