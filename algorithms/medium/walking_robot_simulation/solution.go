package main

import "fmt"

func robotSim(commands []int, obstacles [][]int) int {
	directions := []string{"U", "R", "D", "L"}
	direction, x, y := 0, 0, 0
	farest := 0

	pointMap := make(map[int]map[int]bool, 0)
	for _, obstacle := range obstacles {
		if _, ok := pointMap[obstacle[0]]; !ok {
			pointMap[obstacle[0]] = map[int]bool{}
		}
		pointMap[obstacle[0]][obstacle[1]] = true
	}

	for _, command := range commands {
		switch command {
		case -1:
			direction += 1
			if direction == 4 {
				direction = 0
			}
			continue
		case -2:
			direction -= 1
			if direction == -1 {
				direction = 3
			}
			continue
		}

		switch directions[direction] {
		case "U":
			for i := 0; i < command; i++ {
				y += 1
				if _, ok := pointMap[x]; ok && pointMap[x][y] {
					y -= 1
					break
				}
			}
		case "D":
			for i := 0; i < command; i++ {
				y -= 1
				if _, ok := pointMap[x]; ok && pointMap[x][y] {
					y += 1
					break
				}
			}
		case "L":
			for i := 0; i < command; i++ {
				x -= 1
				if _, ok := pointMap[x]; ok && pointMap[x][y] {
					x += 1
					break
				}
			}
		case "R":
			for i := 0; i < command; i++ {
				x += 1
				if _, ok := pointMap[x]; ok && pointMap[x][y] {
					x -= 1
					break
				}
			}
		}

		if x*x+y*y > farest {
			farest = x*x + y*y
		}
	}

	return farest
}

func main() {
	// Example 1: no obstacles, robot ends at (4,1) → 4²+1²=17... wait, (0,3) after turning right then 3 up
	fmt.Println(robotSim([]int{4, -1, 3}, [][]int{}) == 25)
	// Example 2: obstacle at (2,4) blocks the robot
	fmt.Println(robotSim([]int{4, -1, 4, -2, 4}, [][]int{{2, 4}}) == 65)
	// Example 3: obstacle at origin, robot turns twice then goes 6 steps north
	fmt.Println(robotSim([]int{6, -1, -1, 6}, [][]int{{0, 0}}) == 36)
	// Edge case: empty commands
	fmt.Println(robotSim([]int{}, [][]int{}) == 0)
	// Edge case: turn commands only, robot stays at origin
	fmt.Println(robotSim([]int{-1, -1, -2}, [][]int{}) == 0)
}
