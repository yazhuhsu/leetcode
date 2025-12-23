## 728. Self Dividing Numbers
### Rules
- A self-dividing number is divisible by every digit it contains
- Given a range `[left, right]`, return all self-dividing numbers in that range
- Numbers containing digit `0` are NOT self-dividing (cannot divide by 0)
- Single digit numbers (1-9) are always self-dividing

### Ideas
- Iterate through range from left to right
    ```go
    nums := make([]int, 0, right-left+1)
    for i := left; i <= right; i++ {
        if isDivided(i) {
            nums = append(nums, i)
        }
    }
    ```
- Extract unique digits from number
    ```go
    numMap := make(map[int]bool, len(string(num)))
    strs := strconv.Itoa(num)
    for _, str := range strings.Split(strs, "") {
        r, _ := strconv.Atoi(str)
        numMap[r] = true
    }
    ```
- Check if number is divisible by all its digits
    ```go
    for n, _ := range numMap {
        if n == 0 {
            return false  // cannot divide by 0
        }
        if num%n != 0 {
            return false  // not divisible
        }
    }
    return true
    ```

### Walkthrough (left = 1, right = 22)
```
nums = []
for i := 1; i <= 22; i++:
├─ i=1: isDivided(1)
│  ├─ numMap={1: true}
│  └─ 1%1==0 → true → nums=[1]
├─ i=2: isDivided(2)
│  ├─ numMap={2: true}
│  └─ 2%2==0 → true → nums=[1,2]
├─ i=3: isDivided(3)
│  └─ 3%3==0 → true → nums=[1,2,3]
├─ ... (4-9 all self-dividing) → nums=[1,2,3,4,5,6,7,8,9]
├─ i=10: isDivided(10)
│  ├─ numMap={1: true, 0: true}
│  └─ contains 0 → false
├─ i=11: isDivided(11)
│  ├─ numMap={1: true}
│  └─ 11%1==0 → true → nums=[1,2,3,4,5,6,7,8,9,11]
├─ i=12: isDivided(12)
│  ├─ numMap={1: true, 2: true}
│  ├─ 12%1==0 ✓
│  └─ 12%2==0 ✓ → true → nums=[1,2,3,4,5,6,7,8,9,11,12]
├─ i=13: isDivided(13)
│  ├─ numMap={1: true, 3: true}
│  ├─ 13%1==0 ✓
│  └─ 13%3!=0 ✗ → false
├─ i=14: isDivided(14)
│  └─ 14%4!=0 → false
├─ i=15: isDivided(15)
│  ├─ numMap={1: true, 5: true}
│  ├─ 15%1==0 ✓
│  └─ 15%5==0 ✓ → true → nums=[1,2,3,4,5,6,7,8,9,11,12,15]
├─ i=16: isDivided(16)
│  └─ 16%6!=0 → false
├─ ... (17-21 not self-dividing)
└─ i=22: isDivided(22)
   ├─ numMap={2: true}
   └─ 22%2==0 → true → nums=[1,2,3,4,5,6,7,8,9,11,12,15,22]

return nums = [1,2,3,4,5,6,7,8,9,11,12,15,22]
```

### Result
- Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
- Examples:
  - 12 is self-dividing: 12%1=0, 12%2=0
  - 15 is self-dividing: 15%1=0, 15%5=0
  - 13 is NOT: 13%3≠0
  - 10 is NOT: contains digit 0