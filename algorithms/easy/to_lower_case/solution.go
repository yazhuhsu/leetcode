package main

import (
	"fmt"
	"strings"
)

func toLowerCase(s string) string {
	return strings.ToLower(s)
}

func main() {
	fmt.Println(toLowerCase("Hello") == "hello")
	fmt.Println(toLowerCase("here") == "here")
	fmt.Println(toLowerCase("LOVELY") == "lovely")
}
