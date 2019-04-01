#Insertion Sort

#### By: Tim Schoen
This function for insertion sort that takes in an unsorted array and returns the array sorted using insertion sort.


## Approach  
Start at index 1.   compare it to the value to the left (index 0)  if value at 1 is < the value at 0 swap the to values.  move on down the line...  so Index 4 compare to 3,2, and if necessary 1, and 0. switiching places need be.>


### Efficiency
Big O Time = O(n^2)
Big O Size = O(1)

## Testing

- [x] A randomly generated unsorted array returns the array sorted
- [x] A sorted array returns the same sorted array
- [x] A backwards-sorted array returns the array sorted
- [x] An empty array returns the same empty array
- [x] An array of one element returns the same single-element array


