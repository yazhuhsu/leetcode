package main

func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	j := nums[0]
	i := 1

	for i < len(nums) {
		if nums[i] == j {
			nums = append(nums[:i], nums[i+1:]...)
		} else if j < nums[i] {
			j = nums[i]
			i++
		}

		if i == len(nums) {
			break
		}
	}

	return len(nums)
}

func main() {}
