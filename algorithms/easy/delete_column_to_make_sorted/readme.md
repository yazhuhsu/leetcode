## 944. Delete Columns to Make Sorted
### Rules
- You are given an array of equal-length strings `strs`
- Consider each column (same index across all strings)
- A column is sorted if characters are in non-decreasing order from top to bottom
- Find the minimum number of columns to delete so that each remaining column is sorted

### Ideas
- Iterate through each column index
    ```Python3
    for i in range(0, len(strs[0])):
    ```
- Build the column string by collecting characters from each row
    ```Python3
    column, orders = "", []
    for j in range(0, len(strs)):
        column += strs[j][i]
        orders.append(strs[j][i])
    ```
- Check if column is sorted by comparing with sorted version
    ```Python3
    orders.sort()
    sorted_column = "".join(orders)
    
    if sorted_column != column:
        count += 1
    ```

### Walkthrough (strs = ["cba", "daf", "ghi"])
```
count = 0
for i in range(0, len(strs[0])):
├─ i=0: column="cdg", orders=['c','d','g']
│  ├─ orders.sort() → ['c','d','g']
│  ├─ sorted_column="cdg"
│  └─ sorted_column == column → keep
├─ i=1: column="bah", orders=['b','a','h']
│  ├─ orders.sort() → ['a','b','h']
│  ├─ sorted_column="abh"
│  └─ sorted_column != column → delete, count=1
└─ i=2: column="afi", orders=['a','f','i']
   ├─ orders.sort() → ['a','f','i']
   ├─ sorted_column="afi"
   └─ sorted_column == column → keep

count = 1
```

### Result
- 1 column deleted: column 1 ("bah" is not sorted)

