package main

import (
	"fmt"
	"math"
)

func countPrimeSetBits(left int, right int) int {
	prime := 0
	for i := 0; i <= right-left; i++ {
		num, bits := left+i, 0
		for num > 0 {
			bits += num % 2
			num = num / 2
		}

		if isPrime(bits) {
			prime += 1
		}
	}

	return prime
}

func isPrime(num int) bool {
	if num < 2 {
		return false
	}

	for i := 2; i <= int(math.Sqrt(float64(num))); i++ {
		if num%i == 0 {
			return false
		}
	}

	return true
}

func main() {
	fmt.Println(countPrimeSetBits(6, 10) == 4)
	fmt.Println(countPrimeSetBits(10, 15) == 5)
}
