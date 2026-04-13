## 1848. Minimum Distance to the Target Element

### Rules
- Given an integer array `nums`, an integer `target`, and an integer `start`
- Find every index `i` where `nums[i] == target`
- Return the minimum value of `abs(i - start)` among all such indices
- It is guaranteed that `target` exists in `nums`

### Ideas
- Iterate through `nums`, skip elements that don't equal `target`
- For each matching index, compute `abs(i - start)` and track the minimum

    ```go
    for idx, num := range nums {
        if num != target { continue }
        m := idx - start
        if idx < start { m = start - idx }
        if minimized > m { minimized = m }
    }
    ```

### Walkthrough (`nums = [5, 3, 6, 5], target = 5, start = 2`)

```
idx=0: nums[0]=5 == target
├─ m = |0-2| = 2  →  minimized = 2

idx=1: nums[1]=3 ≠ target → skip

idx=2: nums[2]=6 ≠ target → skip

idx=3: nums[3]=5 == target
└─ m = |3-2| = 1  →  1 < 2, minimized = 1

return 1
```

### Result
- Output: `1`
- Examples:
  - `[5,3,6,5], target=5, start=2` → indices 0 and 3 match; `|3-2|=1` wins → **1**
  - `[1,2,3,4,5], target=5, start=3` → only index 4 matches; `|4-3|=1` → **1**
  - `[1,2,3,4,5], target=1, start=4` → only index 0 matches; `|0-4|=4` → **4**
