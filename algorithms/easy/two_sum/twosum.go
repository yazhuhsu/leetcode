package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func twoSum(nums []int, target int) []int {
	var result []int
	for i := 0; i < len(nums)-1; i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] == target {
				result = append(result, i, j)
				break
			}
		}

		if len(result) == 2 {
			break
		}
	}

	return result
}

func main() {
	file, err := os.Open("two_sum.txt")
	if err != nil {
		log.Fatal(err.Error())
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}

	for i := 0; i < len(lines)-1; i += 2 {
		a := strings.Trim(lines[i], "[]")
		b := strings.Split(a, ", ")
		nums := make([]int, len(b))
		for j, k := range b {
			nums[j], _ = strconv.Atoi(k)
		}
		target, _ := strconv.Atoi(lines[i+1])
		fmt.Println(twoSum(nums, target))
	}
}
