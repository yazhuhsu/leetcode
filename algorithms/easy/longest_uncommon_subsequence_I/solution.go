package main

import "fmt"

func findLUSlength(a string, b string) int {
	first, second := find(a, b), find(b, a)
	if second > first {
		return second
	}

	return first
}

func find(a string, b string) int {
	match := []int{}
	for i := 0; i < len(b); i++ {
		if i+len(a) > len(b) {
			break
		}
		if b[i:i+len(a)] == a {
			match = append(match, i, i+len(a))
		}
	}

	if len(match) == 0 {
		return len(a)
	}

	return -1
}

func main() {
	fmt.Println(findLUSlength("aba", "cdc") == 3)
	fmt.Println(findLUSlength("aaa", "aaa") == -1)
	fmt.Println(findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef") == 17)
	fmt.Println(findLUSlength("aefeaf", "a") == 6)
	fmt.Println(findLUSlength("abab", "cdc") == 4)
}
