# 1277. Count Square Submatrices with All Ones

## Solution
1. Find max square of the matrix.
2. Calculate each square size by shifting one position.

### Walkthrough

For 
`matrix=
    [
        [1,0],
        [1,1]
    ]
`

#### Step 1. Find max square
```
the matrix is 2x2;
the max square is 2x2;
```

### Step 2. Calculate each square size by shifting one position.
```
[
    [1,0],
    [1,1]
]

side = 0
├─ [
│     ↓
│    [1,1],
│    [1,1]
│  ]
│
│  ├─ [1] → 1
│  │  [1,1]
│  └─ [1,1] → 1
└─ 1+1=2
├─ [
│    [1,1],
│     ↓
│    [1,1]
│  ]
│
│  └─ [1] → 1
└─ 1
├─ [
│       ↓
│    [1,1],
│    [1,1]
│  ]
│
│  └─ [1] → 1
└─ 1
├─ [
│    [1,1],
│       ↓
│    [1,1]
│  ]
│
│  └─ [1] → 1
└─ 1

Final: 2+1+1+1=5
```