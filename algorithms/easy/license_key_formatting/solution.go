package main

import (
	"fmt"
	"strings"
)

func licenseKeyFormatting(s string, k int) string {
	chars := strings.Replace(s, "-", "", -1)
	prefixCount := len(chars) % k
	license, group, prefix := "", "", false
	if prefixCount == 0 {
		prefix = true
	}
	for _, c := range chars {
		group += string(c)
		if !prefix && len(group) == prefixCount {
			license += group
			group = ""
			prefix = true
		} else if len(group) == k {
			if license != "" {
				license += "-"
			}
			license += group
			group = ""
		}
	}

	return strings.ToUpper(license)
}

func main() {
	fmt.Println(licenseKeyFormatting("5F3Z-2e-9-w", 4) == "5F3Z-2E9W")
	fmt.Println(licenseKeyFormatting("2-5g-3-J", 2) == "2-5G-3J")
}
