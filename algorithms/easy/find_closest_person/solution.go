package main

import "fmt"

func findClosest(x int, y int, z int) int {
	xDistance, yDistance := z-x, z-y
	if xDistance < 0 {
		xDistance = -xDistance
	}
	if yDistance < 0 {
		yDistance = -yDistance
	}

	if xDistance > yDistance {
		return 2
	} else if xDistance < yDistance {
		return 1
	}

	return 0
}

func main() {
	fmt.Println(findClosest(2, 7, 4) == 1)
	fmt.Println(findClosest(2, 5, 6) == 2)
	fmt.Println(findClosest(1, 5, 3) == 0)
}
