package main

import "fmt"

func longestPalindrome(s string) int {
	// count the number of each rune in the string
	runeMap := make(map[rune]int)
	for _, v := range s {
		if _, ok := runeMap[v]; !ok {
			runeMap[v] = 0
		}

		runeMap[v] += 1
	}

	count, mid := 0, false
	for _, v := range runeMap {
		// even, add the number of the rune
		if v%2 == 0 {
			count += v
		} else {
			// odd, add the number of the rune - 1
			count += v - 1
			// odd, put one rune in the middle
			if !mid {
				count += 1
				mid = true
			}
		}
	}

	return count
}

func main() {
	// 1. runeMap = {a: 1, b: 1, c: 4, d: 2}
	// 2. iterate, a in the middle
	// 3. iterate, b not in palindrome
	// 4. iterate, c, add 4, start = cc, end = cc
	// 5. iterate, d, add 2, start = ccd, end = dcc
	// 6. return 7, ccdadcc/dccaccd
	fmt.Println(longestPalindrome("abccccdd") == 7)
	fmt.Println(longestPalindrome("a") == 1)
	fmt.Println(longestPalindrome("ccc") == 3)
}
