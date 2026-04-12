## 3740. Minimum Distance Between Three Equal Elements I

### Rules
- Given a 0-indexed integer array `nums`
- Find three indices `i < j < k` such that `nums[i] == nums[j] == nums[k]`
- The distance is defined as `(j - i) + (k - j) + (k - i)`
- Return the minimum distance, or `-1` if no such triple exists

### Ideas
- Group indices of each value using a map
- For each value with at least 3 occurrences, slide a window of 3 consecutive indices and compute the distance
- Track the global minimum across all values

    ```go
    goods := make(map[int][]int)
    for idx, num := range nums {
        goods[num] = append(goods[num], idx)
    }
    for _, values := range goods {
        if len(values) < 3 { continue }
        for idx := range len(values) - 2 {
            d := (values[idx+1]-values[idx]) + (values[idx+2]-values[idx+1]) + (values[idx+2]-values[idx])
            // update minimum
        }
    }
    ```

### Walkthrough (`nums = [1, 2, 1, 2, 2, 1]`)

```
Build index map:
├─ 1 → [0, 2, 5]
└─ 2 → [1, 3, 4]

Process value 1:
└─ window [0, 2, 5]:
   ├─ (2-0) = 2
   ├─ (5-2) = 3
   └─ (5-0) = 5  →  d = 2+3+5 = 10  →  distance = 10

Process value 2:
└─ window [1, 3, 4]:
   ├─ (3-1) = 2
   ├─ (4-3) = 1
   └─ (4-1) = 3  →  d = 2+1+3 = 6  →  6 < 10, distance = 6

distance = 6
```

### Result
- Output: `6`
- Examples:
  - `[1,2,1,2,2,1]` → value 2 wins at indices `(1,3,4)`, distance = 2+1+3 = **6**
  - `[1,2,3]` → no value appears 3 times → **-1**
  - `[1,1,1,1]` → best window is `(0,1,2)`, distance = 1+1+2 = **4**
