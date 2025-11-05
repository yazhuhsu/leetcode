package main

import "fmt"

func findComplement(num int) int {
	numStr := ""
	for num != 0 {
		if num%2 == 1 {
			numStr = "0" + numStr
		} else {
			numStr = "1" + numStr
		}

		num = int(num / 2)
	}

	sum, n := 0, 1
	for i := 0; i < len(numStr); i++ {
		if numStr[len(numStr)-1-i] == '1' {
			sum += n
		}

		n = n * 2
	}

	return sum
}

func main() {
	fmt.Println(findComplement(5) == 2)
	fmt.Println(findComplement(1) == 0)
}
