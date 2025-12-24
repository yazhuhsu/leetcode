## 3074. Apple Redistribution into Boxes
### Rules
- Given `apple` array: number of apples in each pack
- Given `capacity` array: capacity of each box
- Find minimum number of boxes needed to store all apples
- Use greedy approach: fill largest boxes first

### Ideas
- Sort boxes by capacity in descending order (largest first)
    ```go
    sort.Slice(capacity, func(i, j int) bool {
        return capacity[i] > capacity[j]
    })
    ```
- Calculate total number of apples
    ```go
    sum := 0
    for _, a := range apple {
        sum += a
    }
    ```
- Fill boxes greedily until all apples are packed
    ```go
    boxes := 0
    for _, cap := range capacity {
        if cap <= sum {
            sum = sum - cap
            boxes += 1
            continue
        }
        if sum > 0 {
            boxes += 1
        }
        break
    }
    ```

### Walkthrough (apple = [1, 3, 2], capacity = [4, 3, 1, 5, 2])
```
Step 1: Sort capacity descending
capacity = [4, 3, 1, 5, 2]
sort.Slice(capacity, descending)
└─ capacity = [5, 4, 3, 2, 1]

Step 2: Calculate total apples
sum = 0
for _, a := range apple:
├─ a=1: sum=1
├─ a=3: sum=4
└─ a=2: sum=6

Step 3: Fill boxes greedily
boxes = 0
for _, cap := range capacity:
├─ cap=5: cap <= sum (5 <= 6)
│  ├─ sum = 6 - 5 = 1
│  └─ boxes = 1
├─ cap=4: cap > sum (4 > 1)
│  ├─ sum > 0 (1 > 0)
│  ├─ boxes = 2
│  └─ break

return boxes = 2
```

### Result
- Output: 2 boxes needed
- Box 1 (capacity 5): holds 5 apples
- Box 2 (capacity 4): holds 1 apple
- Total: 6 apples in 2 boxes