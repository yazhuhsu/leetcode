## 3075. Maximize Happiness of Selected Children
### Rules
- Given `happiness` array: happiness value of each child
- Select `k` children to maximize total happiness
- Each time you select a child, all non-selected children's happiness decreases by 1
- Happiness cannot go below 0
- Return maximum sum of happiness

### Ideas
- Sort happiness in descending order (select happiest first)
    ```go
    sort.Slice(happiness, func(i, j int) bool {
        return happiness[i] > happiness[j]
    })
    ```
- Select first k children with adjusted happiness
    - Child at index `idx` has been affected by `idx` previous selections
    - Actual happiness = `happiness[idx] - idx`
    - Break early if happiness becomes negative (optimization)
    ```go
    maxSum := int64(0)
    for idx, value := range happiness[:k] {
        if value-idx < 0 {
            break
        }
        maxSum += int64(value) - int64(idx)
    }
    ```

### Walkthrough (happiness = [1, 2, 3], k = 2)
```
Step 1: Sort happiness descending
happiness = [1, 2, 3]
sort.Slice(happiness, descending)
└─ happiness = [3, 2, 1]

Step 2: Select k children and calculate adjusted happiness
maxSum = 0
for idx, value := range happiness[:2]:
├─ idx=0, value=3: value-idx = 3-0 = 3
│  ├─ 3 < 0 ? No
│  └─ maxSum = 0 + 3 = 3
└─ idx=1, value=2: value-idx = 2-1 = 1
   ├─ 1 < 0 ? No
   └─ maxSum = 3 + 1 = 4

return maxSum = 4
```

### Walkthrough (happiness = [1, 1, 1, 1], k = 2)
```
Step 1: Sort happiness descending
happiness = [1, 1, 1, 1]
sort.Slice(happiness, descending)
└─ happiness = [1, 1, 1, 1] (no change)

Step 2: Select k children
maxSum = 0
for idx, value := range happiness[:2]:
├─ idx=0, value=1: value-idx = 1-0 = 1
│  ├─ 1 < 0 ? No
│  └─ maxSum = 0 + 1 = 1
└─ idx=1, value=1: value-idx = 1-1 = 0
   ├─ 0 < 0 ? No
   └─ maxSum = 1 + 0 = 1

return maxSum = 1
```

### Result
- Example 1: [1, 2, 3], k=2 → Output: 4
  - Select child with happiness 3 (contributes 3)
  - Select child with happiness 2 (contributes 2-1=1, decreased by 1 selection)
  - Total: 3 + 1 = 4
- Example 2: [1, 1, 1, 1], k=2 → Output: 1
  - Select child with happiness 1 (contributes 1)
  - Select child with happiness 1 (contributes 1-1=0)
  - Total: 1 + 0 = 1
