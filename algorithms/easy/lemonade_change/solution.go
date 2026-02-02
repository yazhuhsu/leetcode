package main

import "fmt"

func lemonadeChange(bills []int) bool {
	changes := map[int]int{}
	for _, cost := range bills {
		change := cost - 5
		for change >= 10 {
			if changes[10] < 1 {
				break
			}
			changes[10] -= 1
			change -= 10
		}
		for change >= 5 {
			if changes[5] < 1 {
				break
			}
			changes[5] -= 1
			change -= 5
		}

		if change > 0 {
			return false
		}

		changes[cost] += 1
	}

	return true
}

func main() {
	fmt.Println(lemonadeChange([]int{5, 5, 5, 10, 20}) == true)
	fmt.Println(lemonadeChange([]int{5, 5, 10, 10, 20}) == false)
}
