package main

import "fmt"

func isPowerOfFour(n int) bool {
	if n == 1 {
		return true
	}

	num, same := 1, false
	for num < n {
		num = num * 4
		if num == n {
			same = true
			break
		}
	}

	return same
}

func main() {
	fmt.Println(isPowerOfFour(16) == true)
	fmt.Println(isPowerOfFour(5) == false)
	fmt.Println(isPowerOfFour(1) == true)
}
