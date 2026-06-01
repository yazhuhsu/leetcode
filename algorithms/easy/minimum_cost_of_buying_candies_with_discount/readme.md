## 2144. Minimum Cost of Buying Candies With Discount

### Rules
- Given an array `cost` where `cost[i]` is the price of the `i`-th candy
- For every 2 candies bought, you get a 3rd candy for free (the cheapest of the 3)
- Choose any 3 candies each time — maximize savings by making the free candy as expensive as possible
- Return the minimum total cost to buy all candies

### Ideas
- Sort descending so the most expensive candies come first
- Every 3rd candy (index 2, 5, 8, …) is free — skip adding its cost

    ```go
    sort.Slice(cost, func(i, j int) bool { return cost[i] > cost[j] })
    for _, c := range cost {
        if bought == 2 { bought = 0; continue }
        costs += c; bought++
    }
    ```

### Walkthrough (`cost = [6, 5, 7, 9, 2, 2]`)

```
Step 1: Sort descending
cost = [9, 7, 6, 5, 2, 2]

Step 2: Iterate and accumulate cost
costs=0, bought=0
├─ c=9: bought=0 → pay 9,  costs=9,  bought=1
├─ c=7: bought=1 → pay 7,  costs=16, bought=2
├─ c=6: bought=2 → FREE,   costs=16, bought=0
├─ c=5: bought=0 → pay 5,  costs=21, bought=1
├─ c=2: bought=1 → pay 2,  costs=23, bought=2
└─ c=2: bought=2 → FREE,   costs=23, bought=0

return 23
```

### Result
- Output: `23`
- Examples:
  - `[1,2,3]` → sorted `[3,2,1]`, free=1 → pay 3+2 = **5**
  - `[3,3,3]` → sorted `[3,3,3]`, free=3 → pay 3+3 = **6**
