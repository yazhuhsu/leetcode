package main

import "fmt"

func hasAlternatingBits(n int) bool {
	if n == 0 || n == 1 {
		return true
	}
	first, second, third := -1, -1, -1
	for n >= 1 {
		first, second = second, third
		if n%2 == 1 {
			third = 1
		} else {
			third = 0
		}

		n = n / 2

		if first == -1 || second == -1 || third == -1 {
			continue
		}
		if (first+second)%2 == 0 || (second+third)%2 == 0 {
			return false
		}
	}

	if (first+second)%2 == 0 || (second+third)%2 == 0 {
		return false
	}

	return true
}

func main() {
	fmt.Println(hasAlternatingBits(5) == true)
	fmt.Println(hasAlternatingBits(7) == false)
	fmt.Println(hasAlternatingBits(11) == false)
}
