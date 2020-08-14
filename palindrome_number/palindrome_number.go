package main

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}

	result := 0
	original := x

	for x > 0 {
		result *= 10
		result += x % 10
		x /= 10
	}

	if result == original {
		return true
	}

	return false
}

func main() {}
