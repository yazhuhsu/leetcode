package main

func scoreOfString(s string) int {
	sum := 0
	for idx, v := range s {
		if idx == 0 {
			continue
		}

		c := int32(v) - int32(s[idx-1])
		if c > 0 {
			sum += int(c)
		} else {
			sum -= int(c)
		}
	}

	return sum
}

func main() {
	testCases := []string{"hello", "zaz"}
	for _, v := range testCases {
		println(scoreOfString(v))
	}
}
