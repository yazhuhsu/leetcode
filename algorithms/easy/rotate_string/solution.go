package main

import "fmt"

func rotateString(s string, goal string) bool {
	for range s {
		if s[1:]+string(s[0]) == goal {
			return true
		}

		s = s[1:] + string(s[0])
	}

	return false
}

func main() {
	fmt.Println(rotateString("abcde", "cdeab") == true)
	fmt.Println(rotateString("abcde", "abced") == false)
	fmt.Println(rotateString("abcde", "abcde") == true)
	fmt.Println(rotateString("a", "a") == true)
	fmt.Println(rotateString("aa", "aa") == true)
}
