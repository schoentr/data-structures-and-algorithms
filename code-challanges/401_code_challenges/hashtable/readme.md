#HashTables

### By: Tim Schoen

 This defines the class of a HashTable.

 * The **add** method takes in a (key, and a value) and addes them to a Hash table.
 
 * The **contains**  method takes in a (key) and returns a boolean,
 
 * The **get** method takes in a (key) and returns  the value of the given key.

 ## Hashing Function

 * The function sums the letters of  the key, by its ascii value.
 * Mutiplies the total sum by a large prime number (599)
 * Floor devides the  by 1026
