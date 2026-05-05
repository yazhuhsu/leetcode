## 61. Rotate List

### Rules
- Given the head of a linked list and an integer `k`, rotate the list to the right by `k` places
- Rotating right by 1 moves the last node to the front
- If `k >= len`, use `k % len` since full rotations cancel out
- Return the new head

### Ideas
- Collect all node values into a slice
- Compute the rotation offset with `k % len`
- Rebuild the list from the rotated slice

    ```go
    new = append(new, origin[len(origin)-k:]...)  // tail portion
    new = append(new, origin[:len(origin)-k]...)  // head portion
    ```

### Walkthrough (`head = [1,2,3,4,5], k = 2`)

```
Collect values: origin = [1, 2, 3, 4, 5], len=5

k=2, not > 5, no mod needed

Split:
├─ origin[5-2:] = origin[3:] = [4, 5]   (tail, becomes new head)
└─ origin[:5-2] = origin[:3] = [1, 2, 3] (head, becomes new tail)

new = [4, 5, 1, 2, 3]

Rebuild list: 4 → 5 → 1 → 2 → 3
```

### Result
- Output: `[4, 5, 1, 2, 3]`
- Examples:
  - `[1,2,3,4,5], k=2` → **[4,5,1,2,3]**
  - `[0,1,2], k=4` → k%3=1 → **[2,0,1]**
  - `[1,2], k=0` → no rotation → **[1,2]**
