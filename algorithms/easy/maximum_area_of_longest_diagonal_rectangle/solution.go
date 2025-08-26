package main

import "fmt"

func areaOfMaxDiagonal(dimensions [][]int) int {
	max := 0
	width, height := 0, 0
	for i := 0; i < len(dimensions); i++ {
		w, h := dimensions[i][0], dimensions[i][1]
		area := w*w + h*h
		if area > max {
			max = area
			width, height = w, h
		} else if area == max && w*h > width*height {
			max = area
			width, height = w, h
		}
	}

	return width * height
}

func main() {
	fmt.Println(areaOfMaxDiagonal([][]int{{9, 3}, {8, 6}}) == 48)
	fmt.Println(areaOfMaxDiagonal([][]int{{3, 4}, {4, 3}}) == 12)
}
