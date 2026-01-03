## 917. Reverse Only Letters
### Rules
- Given a string `s` containing letters and non-letter characters
- Reverse only the letters in the string
- Keep all non-letter characters in their original positions
- Return the resulting string

### Ideas
- Extract all letters from the string
    ```go
    letters := ""
    for _, ch := range s {
        if unicode.IsLetter(ch) {
            letters += string(ch)
        }
    }
    ```
- Build result by iterating through original string
    - If character is a letter: use reversed letter (from end of letters)
    - If character is not a letter: keep it in original position
    ```go
    idx, reversed := 0, ""
    for _, ch := range s {
        if unicode.IsLetter(ch) {
            reversed += string(letters[len(letters)-idx-1])
            idx += 1
            continue
        }
        reversed += string(ch)
    }
    ```

### Walkthrough (s = "ab-cd")
```
Step 1: Extract all letters
letters = ""
for _, ch := range s:
├─ ch='a': IsLetter=true → letters="a"
├─ ch='b': IsLetter=true → letters="ab"
├─ ch='-': IsLetter=false → skip
├─ ch='c': IsLetter=true → letters="abc"
└─ ch='d': IsLetter=true → letters="abcd"

Step 2: Build reversed string
idx=0, reversed=""
for _, ch := range s:
├─ ch='a': IsLetter=true
│  ├─ Use letters[4-0-1] = letters[3] = 'd'
│  ├─ reversed="d"
│  └─ idx=1
├─ ch='b': IsLetter=true
│  ├─ Use letters[4-1-1] = letters[2] = 'c'
│  ├─ reversed="dc"
│  └─ idx=2
├─ ch='-': IsLetter=false
│  └─ reversed="dc-"
├─ ch='c': IsLetter=true
│  ├─ Use letters[4-2-1] = letters[1] = 'b'
│  ├─ reversed="dc-b"
│  └─ idx=3
└─ ch='d': IsLetter=true
   ├─ Use letters[4-3-1] = letters[0] = 'a'
   └─ reversed="dc-ba"

return reversed = "dc-ba"
```

### Walkthrough (s = "a-bC-dEf-ghIj")
```
Step 1: Extract letters
letters = "abCdEfghIj" (10 letters)

Step 2: Build reversed string
idx=0, reversed=""
for _, ch := range s:
├─ ch='a': letter → use letters[9]='j' → reversed="j", idx=1
├─ ch='-': not letter → reversed="j-"
├─ ch='b': letter → use letters[8]='I' → reversed="j-I", idx=2
├─ ch='C': letter → use letters[7]='h' → reversed="j-Ih", idx=3
├─ ch='-': not letter → reversed="j-Ih-"
├─ ch='d': letter → use letters[6]='g' → reversed="j-Ih-g", idx=4
├─ ch='E': letter → use letters[5]='f' → reversed="j-Ih-gf", idx=5
├─ ch='f': letter → use letters[4]='E' → reversed="j-Ih-gfE", idx=6
├─ ch='-': not letter → reversed="j-Ih-gfE-"
├─ ch='g': letter → use letters[3]='d' → reversed="j-Ih-gfE-d", idx=7
├─ ch='h': letter → use letters[2]='C' → reversed="j-Ih-gfE-dC", idx=8
├─ ch='I': letter → use letters[1]='b' → reversed="j-Ih-gfE-dCb", idx=9
└─ ch='j': letter → use letters[0]='a' → reversed="j-Ih-gfE-dCba", idx=10

return reversed = "j-Ih-gfE-dCba"
```

### Result
- Example 1: "ab-cd" → "dc-ba"
  - Letters: a,b,c,d → reversed to d,c,b,a
  - Non-letter '-' stays in position 2
- Example 2: "a-bC-dEf-ghIj" → "j-Ih-gfE-dCba"
  - Letters reversed: abCdEfghIj → jIhgfEdCba
  - Non-letters '-' stay in positions 1, 4, 8
- Example 3: "Test1ng-Leet=code-Q!" → "Qedo1ct-eeLg=ntse-T!"
  - Letters reversed, digits and symbols stay in place
