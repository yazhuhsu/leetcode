## 3120. Count the Number of Special Characters I

### Rules
- Given a string `word`, a character is **special** if it appears in both lowercase and uppercase form in `word`
- Return the count of distinct special characters
- Each character is counted once regardless of how many times it appears

### Ideas
- Collect all lowercase letters and all uppercase letters into separate maps
- For each uppercase letter found, check if its lowercase counterpart exists in the lowercase map

    ```go
    for w := range upperCase {
        if _, exist := lowerCase[strings.ToLower(w)]; exist {
            count++
        }
    }
    ```

### Walkthrough (`word = "aaAbcBC"`)

```
Scan characters:
├─ 'a' → lowercase: {a:1}
├─ 'a' → lowercase: {a:2}
├─ 'A' → uppercase: {A:1}
├─ 'b' → lowercase: {a:2, b:1}
├─ 'c' → lowercase: {a:2, b:1, c:1}
├─ 'B' → uppercase: {A:1, B:1}
└─ 'C' → uppercase: {A:1, B:1, C:1}

Check uppercase keys:
├─ A → 'a' in lowercase? Yes → count=1
├─ B → 'b' in lowercase? Yes → count=2
└─ C → 'c' in lowercase? Yes → count=3

return 3
```

### Result
- Output: `3`
- Examples:
  - `"aaAbcBC"` → a, b, c appear in both cases → **3**
  - `"AbBCc"` → b, c appear in both; A has no lowercase → **2**
  - `"abc"` → no uppercase letters → **0**
