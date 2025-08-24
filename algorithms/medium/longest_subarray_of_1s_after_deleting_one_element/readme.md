# 1493. Longest Subarray of 1's After Deleting One Element

## Problem Description
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

## Examples

### Example 1:
```
Input: nums = [1,1,0,1]
Output: 3

Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
```

### Example 2:
```
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5

Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
```

### Example 3:
```
Input: nums = [1,1,1]
Output: 2

Explanation: You must delete one element.
```

## Constraints:
- `1 <= nums.length <= 105`
- `nums[i] is either 0 or 1.`

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