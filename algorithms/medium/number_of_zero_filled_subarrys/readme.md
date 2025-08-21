# 2348. Number of Zero-Filled Subarrays

## Problem Description 

Given an integer array nums, return the number of subarrays filled with 0.
A subarray is a contiguous non-empty sequence of elements within an array.

## Examples

### Example 1:
```
Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
```

### Example 2:
```
Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
```

### Example 3:
```
Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.
```

## Constraints:
- `1 <= nums.length <= 105`
- `-109 <= nums[i] <= 109`

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