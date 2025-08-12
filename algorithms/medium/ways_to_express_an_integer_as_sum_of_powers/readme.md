# 2787. Ways to Express an Integer as Sum of Powers

## Problem Description

Given two positive integers `n` and `x`, return the number of ways `n` can be expressed as the sum of the xth power of unique positive integers. In other words, find the number of sets of unique integers `[n1, n2, ..., nk]` where `n = n1^x + n2^x + ... + nk^x`.

Since the combinations can be very large, return it modulo `10^9 + 7`.

**Example**: If `n = 160` and `x = 3`, one way to express `n` is `n = 2^3 + 3^3 + 5^3`.

## Examples

### Example 1
```
Input: n = 10, x = 2
Output: 1
Explanation: We can express n as: n = 3^2 + 1^2 = 10.
             It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.
```

### Example 2
```
Input: n = 4, x = 1
Output: 2
Explanation: We can express n in the following ways:
            - n = 4^1 = 4
            - n = 3^1 + 1^1 = 4
```

## Constraints
- `1 <= n <= 300`
- `1 <= x <= 5`

## Solution: Runtime Error

### Approach
1. Find all numbers from 1 to n where `i^x <= n`, add to `possibleNums`
2. Generate all possible combinations of different sizes from `possibleNums`
3. Check which combinations sum to `n` when raised to power `x`

### Algorithm Walkthrough

For `n=10, x=2`:

#### Step 1: Find Possible Numbers
```
possibleNums = []
for i := 1; i <= 10; i++
├─ i=1: 1^2 = 1 < 10, Add possibleNums[0]=1
├─ i=2: 2^2 = 4 < 10, Add possibleNums[1]=2  
├─ i=3: 3^2 = 9 < 10, Add possibleNums[2]=3
└─ i=4: 4^2 = 16 > 10, Break

Final possibleNums = [1, 2, 3]
```

#### Step 2: Generate Combinations

**1-Element Combinations:**
```
Call: generate(0, [], [1,2,3], 1, [][])
├─ i=0: Add 1 → [1] → BASE CASE → combinations = [[1]]
├─ i=1: Add 2 → [2] → BASE CASE → combinations = [[1],[2]]  
└─ i=2: Add 3 → [3] → BASE CASE → combinations = [[1],[2],[3]]

Final: [[1], [2], [3]]
```

**2-Element Combinations:**
```
Call: generate(0, [], [1,2,3], 2, [][])
├─ i=0: Add 1 → [1]
│  ├─ i=1: Add 2 → [1,2] → BASE CASE → combinations = [[1,2]]
│  └─ i=2: Add 3 → [1,3] → BASE CASE → combinations = [[1,2],[1,3]]
├─ i=1: Add 2 → [2]
│  └─ i=2: Add 3 → [2,3] → BASE CASE → combinations = [[1,2],[1,3],[2,3]]
└─ i=2: Add 3 → [3] → No more elements

Final: [[1,2], [1,3], [2,3]]
```

**3-Element Combinations:**
```
Call: generate(0, [], [1,2,3], 3, [][])
├─ i=0: Add 1 → [1]
│  ├─ i=1: Add 2 → [1,2]
│  │  └─ i=2: Add 3 → [1,2,3] → BASE CASE → combinations = [[1,2,3]]
│  └─ i=2: Add 3 → [1,3] → No more elements
├─ i=1: Add 2 → [2]
│  └─ i=2: Add 3 → [2,3] → No more elements
└─ i=2: Add 3 → [3] → No more elements

Final: [[1,2,3]]
```

#### Step 3: Check Valid Combinations
```
Check each combination:
├─ [1]: 1^2 = 1 ≠ 10 ❌
├─ [2]: 2^2 = 4 ≠ 10 ❌  
├─ [3]: 3^2 = 9 ≠ 10 ❌
├─ [1,2]: 1^2 + 2^2 = 1 + 4 = 5 ≠ 10 ❌
├─ [1,3]: 1^2 + 3^2 = 1 + 9 = 10 ✅
├─ [2,3]: 2^2 + 3^2 = 4 + 9 = 13 ≠ 10 ❌
└─ [1,2,3]: 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14 ≠ 10 ❌

Result: 1 valid combination
```