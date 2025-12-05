package main

import "fmt"

func canPlaceFlowers(flowerbed []int, n int) bool {
	if len(flowerbed) == 1 && flowerbed[0] == 0 {
		return n <= 1
	}

	count := 0
	for idx, bed := range flowerbed {
		if idx == 0 {
			if bed == 0 && flowerbed[1] == 0 {
				count = 1
				flowerbed[0] = 1
			}
			continue
		}

		if idx == len(flowerbed)-1 {
			if bed == 0 && flowerbed[idx-1] == 0 {
				count += 1
				flowerbed[idx] = 1
			}
			continue
		}

		if bed == 0 && flowerbed[idx-1] == 0 && flowerbed[idx+1] == 0 {
			count += 1
			flowerbed[idx] = 1
			continue
		}
	}

	if n <= count {
		return true
	}

	return false
}

func main() {
	fmt.Println(canPlaceFlowers([]int{1, 0, 0, 0, 1}, 1) == true)
	fmt.Println(canPlaceFlowers([]int{1, 0, 0, 0, 1}, 2) == false)
}
