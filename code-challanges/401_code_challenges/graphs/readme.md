#Graph

### By: Tim Schoen

 This defines the class of a Graph.

 * The **add** method takes in a value and adds the vertex to the table
 
 * The **add_edge**  this method takes in two verticies and an optional weight (the default weight is 1) and adds an edge between the two verticies
 
 * The **get_vertices** this method returns a list of all the vertices in the graph
 * The **size**  method return the number of verticies in the graph
 * The **get_neighbors**  method takes in a given vertex and returns its neighbors, and the weight of the edge.   This is returned as a list of tuples (neighbor, weight) 



## Testing
- [x] Node can be successfully added to the graph
- [x] An edge can be successfully added to the graph
- [x] A collection of all nodes can be properly retrieved from the graph
- [x] All appropriate neighbors can be retrieved from the graph
- [x] Neighbors are returned with the weight between nodes included
- [x] The proper size is returned, representing the number of nodes in the graph
- [x] An empty graph properly returns null
