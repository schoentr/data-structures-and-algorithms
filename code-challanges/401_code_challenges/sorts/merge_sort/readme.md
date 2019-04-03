# Merge Sort
#### By: Tim Schoen
This function for insertion sort that takes in an unsorted array and returns the array sorted using a merge sort.


## Approach  
Take in the array,  and split array, in half recursively, until length of array is 1.
Compare single item arrays,  and append them to the original list.


### Efficiency
Big O Time = O(n^2)
Big O Size = O(1)

## Testing
- [x] Tested lists of both numbers and strings(letters)
- [x] A randomly generated unsorted array returns the array sorted
- [x] A sorted array returns the same sorted array
- [x] A backwards-sorted array returns the array sorted
- [x] An empty array returns the same empty array
- [x] An array of one element returns the same single-element array
