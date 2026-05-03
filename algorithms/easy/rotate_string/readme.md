## 796. Rotate String

### Rules
- Given strings `s` and `goal`, return `true` if `goal` is a rotation of `s`
- A rotation shifts all characters of `s` left by one: `s = s[1:] + s[0]`
- `goal` is a rotation if it can be reached by applying this shift any number of times
- Both strings must have the same length

### Ideas
- Rotate `s` one step at a time, comparing against `goal` after each rotation
- If no match after `len(s)` rotations, return false

    ```go
    for range s {
        if s[1:]+string(s[0]) == goal {
            return true
        }
        s = s[1:] + string(s[0])
    }
    ```

### Walkthrough (`s = "abcde", goal = "cdeab"`)

```
rotation 1: "abcde" → "bcdea" == "cdeab"? No
rotation 2: "bcdea" → "cdeab" == "cdeab"? Yes → return true
```

### Result
- Output: `true`
- Examples:
  - `s="abcde", goal="cdeab"` → rotate left 2 times → **true**
  - `s="abcde", goal="abced"` → no rotation produces this → **false**
  - `s="abcde", goal="abcde"` → after 5 rotations returns to original → **true**
