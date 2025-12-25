## 2769. Find the Maximum Achievable Number
### Rules
- Given integers `num` and `t`
- You can perform `t` operations
- Each operation: increment or decrement `num` by 1, AND increment or decrement `x` by 1
- Goal: Find maximum value of `x` such that `num` can equal `x` after `t` operations

### Ideas
- To maximize `x`, use optimal strategy:
  - Set `x = num + 2t` (maximum possible value)
  - In each operation: increment `num` by 1 AND decrement `x` by 1
  - This moves both values toward each other
  - After `t` operations: both equal `num + t`
- Formula: `x = num + 2t`
    ```go
    func theMaximumAchievableX(num int, t int) int {
        return num + t*2
    }
    ```

### Walkthrough (num = 4, t = 1)
```
Strategy: Set x to maximum, then move num and x toward each other
├─ Calculate maximum x: x = num + 2t = 4 + 2*1 = 6
│
├─ Initial state: num=4, x=6
│
├─ Operation 1:
│  ├─ Increment num: 4 → 5
│  └─ Decrement x: 6 → 5
│
└─ After 1 operation: num=5, x=5 ✓ (equal)

return x = 6
```

### Walkthrough (num = 3, t = 2)
```
Strategy: Set x to maximum, then move num and x toward each other
├─ Calculate maximum x: x = num + 2t = 3 + 2*2 = 7
│
├─ Initial state: num=3, x=7
│
├─ Operation 1:
│  ├─ Increment num: 3 → 4
│  └─ Decrement x: 7 → 6
│
├─ Operation 2:
│  ├─ Increment num: 4 → 5
│  └─ Decrement x: 6 → 5
│
└─ After 2 operations: num=5, x=5 ✓ (equal)

return x = 7
```

### Result
- Example 1: num=4, t=1 → x = 4 + 2(1) = 6
  - Strategy: Increment num, decrement x each operation
  - After 1 operation: num=5, x=5 (meet at num+t)
- Example 2: num=3, t=2 → x = 3 + 2(2) = 7
  - After 2 operations: num=5, x=5 (meet at num+t)
- Key insight: Each operation closes gap by 2 (num+1, x-1), so max x = num + 2t