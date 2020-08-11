package main

import "math"

func reverse(x int) int {
	result := 0
	m := int(math.Pow(2, 31))

	for x != 0 {
		if result*10 > -m && result*10 < m-1 {
			result = result * 10
			result += x % 10
			x /= 10
		} else {
			return 0
		}
	}

	return result
}

func main() {}
