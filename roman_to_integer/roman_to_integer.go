package main

import "strings"

func romanToInt(s string) int {
	r := strings.Split(s, "")
	result := 0

	for i := 0; i < len(r); i++ {
		switch r[i] {
		case "I":
			if i != len(r)-1 {
				if r[i+1] == "V" || r[i+1] == "X" {
					result--
				} else {
					result++
				}
			} else {
				result++
			}

		case "V":
			result += 5

		case "X":
			if i != len(r)-1 {
				if r[i+1] == "L" || r[i+1] == "C" {
					result -= 10
				} else {
					result += 10
				}
			} else {
				result += 10
			}

		case "L":
			result += 50

		case "C":
			if i != len(r)-1 {
				if r[i+1] == "D" || r[i+1] == "M" {
					result -= 100
				} else {
					result += 100
				}
			} else {
				result += 100
			}

		case "D":
			result += 500

		case "M":
			result += 1000
		}
	}

	if result >= 1 && result <= 3999 {
		return result
	}
	return 0
}

func main() {}
