## 657. Robot Return to Origin
### Rules
- A robot starts at position `(0, 0)` on a 2D plane
- Given a string `moves` of characters `U`, `D`, `L`, `R` representing direction
- Return `true` if the robot returns to the origin after all moves, `false` otherwise

### Ideas
- Track x and y offsets using a direction map
    ```go
    movements := map[string][]int{
        "R": {1, 0},
        "L": {-1, 0},
        "U": {0, 1},
        "D": {0, -1},
    }
    ```
- Accumulate position for each move, then check if both x and y are 0
    ```go
    origin := []int{0, 0}
    for _, move := range strings.Split(moves, "") {
        origin[0] += movements[move][0]
        origin[1] += movements[move][1]
    }
    return origin[0] == 0 && origin[1] == 0
    ```

### Walkthrough (moves = "UDLR")
```
origin = [0, 0]
├─ move="U": origin[1] += 1 → origin=[0, 1]
├─ move="D": origin[1] -= 1 → origin=[0, 0]
├─ move="L": origin[0] -= 1 → origin=[-1, 0]
└─ move="R": origin[0] += 1 → origin=[0, 0]

origin[0]==0 && origin[1]==0 → true
```

### Result
- Output: `true`
- Examples:
  - `"UD"` → y cancels out, x unchanged → `true`
  - `"LL"` → x=-2, y=0 → `false`
  - `""` → no moves, stays at origin → `true`
