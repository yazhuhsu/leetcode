package main

import "fmt"

func checkRecord(s string) bool {
	absentCount, lateCount := 0, 0
	isConsecutive, consecutive := false, []int{}
	for i := 0; i < len(s); i++ {
		if s[i] == 'A' {
			absentCount += 1
		}
		if s[i] == 'L' {
			if !isConsecutive {
				isConsecutive = true
				consecutive = append(consecutive, i)
			}
		} else if isConsecutive {
			isConsecutive = false
			consecutive = append(consecutive, i-1)
		}
	}

	if isConsecutive {
		consecutive = append(consecutive, len(s)-1)
	}

	for i := 0; i < len(consecutive); i += 2 {
		diff := consecutive[i+1] - consecutive[i] + 1
		if lateCount < diff {
			lateCount = diff
		}
	}

	if absentCount >= 2 || lateCount >= 3 {
		return false
	}

	return true
}

func main() {
	fmt.Println(checkRecord("PPALLP") == true)
	fmt.Println(checkRecord("PPALLL") == false)
}
