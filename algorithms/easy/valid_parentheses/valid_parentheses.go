package main

func isValid(s string) bool {

	if len(s) == 0 {
		return true
	}
	if len(s)%2 == 1 {
		return false
	}

	if s[0] == ')' || s[0] == ']' || s[0] == '}' {
		return false
	}
	if s[len(s)-1] == '(' || s[len(s)-1] == '[' || s[len(s)-1] == '{' {
		return false
	}

	var ss []rune
	ssLen := 0
	for i := 0; i < len(s); i++ {
		if s[i] == '(' || s[i] == '[' || s[i] == '{' {
			ss = append(ss, rune(s[i]))
			ssLen++
		} else if s[i] == ')' {
			if ss[ssLen-1] != '(' {
				return false
			} else if ss[ssLen-1] == '(' {
				ss = ss[:ssLen-1]
				ssLen--
			}
		} else if s[i] == ']' {
			if ss[ssLen-1] != '[' {
				return false
			} else if ss[ssLen-1] == '[' {
				ss = ss[:ssLen-1]
				ssLen--
			}
		} else if s[i] == '}' {
			if ss[ssLen-1] != '{' {
				return false
			} else if ss[ssLen-1] == '{' {
				ss = ss[:ssLen-1]
				ssLen--
			}
		}
	}

	return true
}

func main() {

}
