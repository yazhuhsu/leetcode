package main

import (
	"fmt"
	"strconv"
)

func rotatedDigits(n int) int {
	rotateMap := map[rune]string{
		'0': "0",
		'1': "1",
		'2': "5",
		'5': "2",
		'6': "9",
		'8': "8",
		'9': "6",
	}

	count := 0
	for i := 1; i < n+1; i++ {
		origin, new := strconv.Itoa(i), ""
		for _, c := range strconv.Itoa(i) {
			if _, ok := rotateMap[c]; !ok {
				break
			}

			new += rotateMap[c]
		}

		if len(origin) == len(new) && origin != new {
			count += 1
		}
	}

	return count
}

func main() {
	fmt.Println(rotatedDigits(10) == 4)
	fmt.Println(rotatedDigits(1) == 0)
	fmt.Println(rotatedDigits(2) == 1)
	fmt.Println(rotatedDigits(3) == 1)
	fmt.Println(rotatedDigits(100) == 40)
}
