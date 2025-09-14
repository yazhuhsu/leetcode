# 3195. Find the Minimum Area to Cover All Ones I

## Solution
1. Find the topmost, downmost, leftmost, and rightmost coordinates.
2. Extract row values from the topmost and downmost points, and column values from the leftmost and rightmost points.
3. Calculate the width and height.

### Walkthrough

For 
`grid=
    [
        [0,1,0],
        [1,0,1]
    ]
`

#### Step 1. Find the topmost, downmost, leftmost, and rightmost coordinates.
```
[
    [0,1,0],
    [1,0,1]
]

top, down
├─ [
│      ↓
│   → [0,1,0],
│     [1,0,1] ←
│  ]
├─ [
│        ↓
│   → [0,1,0],
│     [1,0,1] 
│  ]
└─ top: 0, down 1

left, right
├─ [
│      ↓
│   → [0,1,0],
│     [1,0,1] ←
│          ↑ 
│  ]
├─ [
│      ↓
│     [0,1,0],
│   → [1,0,1] 
│  ]
└─ left: 0, right: 2

Final: (1-0+1)*(2-0+1)=6
```