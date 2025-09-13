package main

import "fmt"

func maxFreqSum(s string) int {
	freq, other := make(map[rune]int, 5), make(map[rune]int, 21)
	maxFreq, maxOther := 0, 0
	for _, v := range s {
		if v == 'a' || v == 'e' || v == 'i' || v == 'o' || v == 'u' {
			freq[v] += 1
			continue
		}
		other[v] += 1
	}

	for _, v := range freq {
		if v > maxFreq {
			maxFreq = v
		}
	}

	for _, v := range other {
		if v > maxOther {
			maxOther = v
		}
	}

	return maxFreq + maxOther
}

func main() {
	answers := map[string]int{
		"successes": 6,
		"aeiaeia":   3,
	}

	for n, answer := range answers {
		fmt.Println(maxFreqSum(n) == answer)
	}
}
