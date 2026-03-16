package main

import (
	"fmt"
	"strconv"
	"strings"
)

func daysBetweenDates(date1 string, date2 string) int {
	days1 := daysSince1971(date1)
	days2 := daysSince1971(date2)

	if days1 > days2 {
		return days1 - days2
	}

	return days2 - days1
}

func daysSince1971(date string) int {
	days := 0
	dates := strings.Split(date, "-")

	year, _ := strconv.Atoi(dates[0])
	month, _ := strconv.Atoi(dates[1])
	day, _ := strconv.Atoi(dates[2])
	for y := 1971; y < year; y++ {
		days += daysInYear(y)
	}
	for m := 1; m < month; m++ {
		days += daysInMonth(year, m)
	}

	days += day

	return days
}

func daysInMonth(year int, month int) int {
	switch month {
	case 1, 3, 5, 7, 8, 10, 12:
		return 31
	case 4, 6, 9, 11:
		return 30
	case 2:
		if isLeapYear(year) {
			return 29
		} else {
			return 28
		}
	}

	return 0
}

func daysInYear(year int) int {
	if isLeapYear(year) {
		return 366
	}

	return 365
}

func isLeapYear(year int) bool {
	if year%4 != 0 {
		return false
	} else if year%4 == 0 && year%100 != 0 {
		return true
	} else if year%100 == 0 && year%400 != 0 {
		return false
	} else if year%400 == 0 {
		return true
	}

	return false
}

func main() {
	fmt.Println(daysBetweenDates("2019-06-29", "2019-06-30") == 1)
	fmt.Println(daysBetweenDates("2020-01-15", "2019-12-31") == 15)
}
