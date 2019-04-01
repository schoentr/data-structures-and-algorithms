#Left Join

#### By: Tim Schoen
This challenge  is to take in two hash tables,   and join the two on the matching keys,  if the seccond hash table does not have the key in the table, the value placed will be `None`
## Approach  
* Take in two Hash Tables
* Itterate over each index in the first hash table.
    * with-in each index itterate over the linked-list
    * see if key in the first hash table, is in the seccond hash table
        * if so append  to return list[key, value from Hash Table 1, value from Hash Table 2]
        * if not append to return list [key, value from Hash Table 1, None]

### Efficiency
Big O Time = O(n)
Big O Size = O(n)



## Solution
https://github.com/schoentr/data-structures-and-algorithms/blob/master/code-challanges/401/assets/left_join.jpg