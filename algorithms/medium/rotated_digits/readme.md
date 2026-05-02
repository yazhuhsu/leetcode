## 788. Rotated Digits

### Rules
- A number is **good** if, after rotating each digit 180°, it forms a valid and *different* number
- Valid digits after rotation: `0→0`, `1→1`, `2→5`, `5→2`, `6→9`, `8→8`, `9→6`
- Invalid digits (can't be rotated): `3`, `4`, `7`
- A number is good only if all its digits are valid **and** the rotated result differs from the original
- Given `n`, return the count of good numbers in the range `[1, n]`

### Ideas
- For each number, rotate every digit using a map
- If any digit is invalid, stop early (the number can't be good)
- After rotating all digits, compare the result to the original — it must differ

    ```go
    for _, c := range strconv.Itoa(i) {
        if _, ok := rotateMap[c]; !ok {
            break  // invalid digit, skip this number
        }
        new += rotateMap[c]
    }
    if len(origin) == len(new) && origin != new {
        count++
    }
    ```

### Walkthrough (`n = 10`)

```
i=1:  "1" → "1"  same     → not good
i=2:  "2" → "5"  different → good   count=1
i=3:  "3" → invalid digit  → not good
i=4:  "4" → invalid digit  → not good
i=5:  "5" → "2"  different → good   count=2
i=6:  "6" → "9"  different → good   count=3
i=7:  "7" → invalid digit  → not good
i=8:  "8" → "8"  same      → not good
i=9:  "9" → "6"  different → good   count=4
i=10: "10" → "10" same     → not good

return 4
```

### Result
- Output: `4`
- Examples:
  - `n=10` → good numbers are 2, 5, 6, 9 → **4**
  - `n=2`  → only 2 is good → **1**
  - `n=100` → **40**
