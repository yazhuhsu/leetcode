# 2348. Number of Zero-Filled Subarrays

## Solution
1. Find start and end for 0 in array.
2. Calculate combinations for each start and end with displacement.

### Walkthrough

For `nums=[1,3,0,0,2,0,0,4]`

#### Step 1. Find start and end
```
starts, ends = [], []
flag = -1
for i := 0; i < len(nums); i++
├─ i=0: 1, continue
├─ i=1: 3, continue
├─ i=2: 0, add starts[0]=2, set flag=2
├─ i=3: 0, flag=2, continue
├─ i=4: 2, add ends[0]=3, set flag=-1
├─ i=5: 0, add starts[1]=5, set flag=5
├─ i=6: 0, flag=5, continue
└─ i=7: 4, add ends[1]=6
```

#### Step 2. Calculate with displacement
```
for i := 0; i < len(starts); i++
├─ i=0: start=2,end=3 → length=3-2+1=2
├──for j := 0; j < 2; j ++
│  ├─ j=0: 2-0=2 → [0],[0,0]
│  └─ j=1: 2-1=1 → [0]
├─ i=1: start=5,end=6 → length=6-5+1=2
├──for j := 0; j < 2; j ++
│  ├─ j=0: 2-0=2 → [0], [0,0]
│  └─ j=1: 2-1=1 → [0]

Final: 3+3=6
```