## 70. Climbing Stairs
### Rules
- It takes `n` steps to reach the top
- Each time you can either climb `1` or `2` steps
- Find distinct ways to climb

### Ideas
- Calculate 2-step times
    ```Python3
    for double_step in range(0, n):
    ```
- Calculate 1-step times
    ```Python3
    single_step = n - 2 * double_step
    ```
- Calculate combinations: 
    - C(step, single_step) = step! / (single_step! × double_step!)
    - Represents: "How many ways to arrange these steps?"
    ```Python3
    denominator = 1  # builds numerator
    molecular = 1    # builds denominator
    for i in range(1, single_step + 1):
        denominator = denominator * (step + 1 - i)
        molecular = molecular * i
                    
    steps = steps + int(denominator / molecular)
    ```

### Walkthrough (n = 3)
```
steps = 0
for double_step in range(0, n):
├─ double_step=0: single_step=3, step=3 (total moves)
├──for i in range(1, single_step + 1):
│  ├─ i=1: denominator=3, molecular=1
│  ├─ i=2: denominator=6, molecular=2
│  └─ i=3: denominator=6, molecular=6
│  └─ C(3,3) = 6/6 = 1
├─ double_step=1: single_step=1, step=2
├──for i in range(1, single_step + 1):
│  └─ i=1: denominator=2, molecular=1
│  └─ C(2,1) = 2/1 = 2

steps = C(3,3) + C(2,1) = 1 + 2 = 3
```

### Result
- 3 ways: [1,1,1], [2,1], [1,2]