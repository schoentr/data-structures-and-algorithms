#Quick Sort

#### By: Tim Schoen
This function for insertion sort that takes in an unsorted array and returns the array sorted using quick sort.


## Approach  
Take the list,  and find a pivot point on the array,  moving from the outside in swap values that are higher the the value at the pivot point and values that are lower.   when the positions meet, swap.  The function will recusively call the left side and the right side  thus sorting the list.

### Efficiency
Big O Time = O(n^2) worst case,   ususally 0 (n logn)
Big O Size = O(n)

## Testing
- [x] Tested lists of both numbers and strings(letters)
- [x] A randomly generated unsorted array returns the array sorted
- [x] A sorted array returns the same sorted array
- [x] A backwards-sorted array returns the array sorted
- [x] An empty array returns the same empty array
- [x] An array of one element returns the same single-element array
