## 874. Walking Robot Simulation

### Rules
- A robot starts at the origin `(0, 0)` facing north
- Given a list of commands and a set of obstacles on an infinite grid
- Commands: `-2` turn left 90°, `-1` turn right 90°, `1–9` move that many steps north
- If a step would land on an obstacle, the robot stops just before it and processes the next command
- Return the maximum Euclidean distance squared (`x² + y²`) reached at any point

### Ideas
- Store obstacles in a nested map for O(1) lookup
- Track current direction with an index into `["U", "R", "D", "L"]`; turn right increments, turn left decrements (mod 4)
- After each move command, update `farest` if the new distance is larger

    ```go
    pointMap := make(map[int]map[int]bool)
    for _, obs := range obstacles {
        if pointMap[obs[0]] == nil {
            pointMap[obs[0]] = map[int]bool{}
        }
        pointMap[obs[0]][obs[1]] = true
    }
    ```

### Walkthrough (`commands = [4, -1, 3], obstacles = []`)

```
Start: dir=U x=0 y=0 farest=0

Command 4 (move 4 steps north):
├─ step 1: y=1, no obstacle → continue
├─ step 2: y=2, no obstacle → continue
├─ step 3: y=3, no obstacle → continue
└─ step 4: y=4, no obstacle → farest = max(0, 0²+4²) = 16

Command -1 (turn right):
└─ dir: U → R

Command 3 (move 3 steps east):
├─ step 1: x=1, no obstacle → continue
├─ step 2: x=2, no obstacle → continue
└─ step 3: x=3, no obstacle → farest = max(16, 3²+4²) = 25
```

### Result
- Output: `25`
- Examples:
  - `[4,-1,3], []` → robot reaches `(3,4)`, max distance² = 3²+4² = **25**
  - `[4,-1,4,-2,4], [[2,4]]` → obstacle at `(2,4)` stops eastward move at `(1,4)`, then robot goes back north to `(1,8)`, max = 1²+8² = **65**
