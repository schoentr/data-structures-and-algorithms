# Get Edges

## Challenge
 Problem Domain:  Given a graph and a list of values. Find the total weight to get to the desitnation
## Approach & Efficiency
Travers across the list given to traverse.
Origin = list[i]
Destination = list [i+1]
Find the neighbors of origin, if desiantion is a neighbor add weight to sum and move to next element on list.
If destination is not a neighbor return False.
after finished traversing across list return sum


## Solution
https://github.com/schoentr/data-structures-and-algorithms/blob/master/code-challanges/401/assets/get_edges.jpg