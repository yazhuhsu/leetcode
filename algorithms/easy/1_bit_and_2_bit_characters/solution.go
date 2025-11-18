package main

import "fmt"

func isOneBitCharacter(bits []int) bool {
	skip := false
	for i := 0; i < len(bits)-1; i++ {
		if skip {
			skip = false
			continue
		}

		if bits[i] == 1 {
			skip = true
			continue
		}
	}

	if skip {
		return false
	}

	return true
}

func main() {
	fmt.Println(isOneBitCharacter([]int{1, 0, 0}) == true)
	fmt.Println(isOneBitCharacter([]int{1, 1, 1, 0}) == false)
}
