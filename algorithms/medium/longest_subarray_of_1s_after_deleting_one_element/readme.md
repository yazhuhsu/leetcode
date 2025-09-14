# 1493. Longest Subarray of 1's After Deleting One Element

## Solution
1. Find all zero indexes
2. Walk through all zero indexes, calculate the max length by removing one of the zeros

### Walkthrough

For `nums=[0,1,1,1,0,1,1,0,1]`

#### Step 1. Find all zeros
```
zeros=[0,4,7]
```

### Step 2. calculate the max length
```
max = 0
for i := 0; i < len(zeros); i++
├─ i=0: 0, start=0,end=3; max=3-0=3
├─ i=1: 4, start=1,end=6; max=6-1=5
└─ i=2: 7, start=5,end=8; max=8-5=3

Final: 5
```