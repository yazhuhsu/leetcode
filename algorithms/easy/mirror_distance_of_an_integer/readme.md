## 3783. Mirror Distance of an Integer

### Rules
- Given a positive integer `n`, compute its **mirror**: reverse the digits of `n`
- Return the absolute difference between `n` and its mirror
- Leading zeros in the mirror are dropped (i.e., treat the reversed number as a plain integer)

### Ideas
- Reverse digits by repeatedly taking `n % 10` as the next digit of the mirror, then dividing `n` by 10
- Build the mirror by placing each extracted digit at the correct power of 10
- Return `abs(n - mirror)`

    ```go
    copy, mirror := n, 0
    for i := 1; i < len(strconv.Itoa(n))+1; i++ {
        mirror += (copy % 10) * int(math.Pow(10, float64(len(strconv.Itoa(n))-i)))
        copy /= 10
    }
    ```

### Walkthrough (`n = 1234`)

```
digits = 4, copy=1234, mirror=0

i=1: copy%10=4, place at 10^3=1000  →  mirror += 4000  →  mirror=4000, copy=123
i=2: copy%10=3, place at 10^2=100   →  mirror += 300   →  mirror=4300, copy=12
i=3: copy%10=2, place at 10^1=10    →  mirror += 20    →  mirror=4320, copy=1
i=4: copy%10=1, place at 10^0=1     →  mirror += 1     →  mirror=4321, copy=0

mirror=4321 > n=1234  →  return 4321-1234 = 3087
```

### Improvements
- Renamed `copy` → `num` to avoid shadowing the built-in `copy` (Go) / `copy` module (Python)
- Replaced `math.Pow` + `strconv.Itoa` with a single loop using `mirror = mirror*10 + num%10` — no float arithmetic, no precomputed digit count needed
- Replaced float division `/` with integer division `//` in Python

    ```go
    // single loop: shift mirror left and append last digit of num
    num, mirror := n, 0
    for num > 0 {
        mirror = mirror*10 + num%10
        num /= 10
    }
    ```

### Result
- Output: `3087`
- Examples:
  - `n=1234` → mirror=4321, `|4321-1234|` = **3087**
  - `n=1221` → mirror=1221 (palindrome), `|1221-1221|` = **0**
  - `n=100`  → mirror=1 (leading zeros dropped), `|1-100|` = **99**
