package main

import (
	"fmt"
	"math"
	"strconv"
)

func maximum69Number(num int) int {
	str, maxNum := strconv.Itoa(num), num
	for i := 0; i < len(str); i++ {
		if string(str[i]) == "6" {
			count := num + 3*int(math.Pow(10, float64(len(str)-i-1)))
			if count > maxNum {
				maxNum = count
			}
		}
	}

	return maxNum
}

func main() {
	fmt.Println(maximum69Number(9669) == 9969)
	fmt.Println(maximum69Number(9996) == 9999)
	fmt.Println(maximum69Number(9999) == 9999)
}
