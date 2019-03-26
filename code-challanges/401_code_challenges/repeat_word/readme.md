# Repeated Word
Tim Schoen

### Challenge:
* Write a function that accepts a lengthy string parameter.
 * Without utilizing any of the built-in library methods available to your language, return the first word to occur more than once in that provided string.

## Approach & Efficiency
* I chose to use a HashTable because of its efficiency. 
* I choose to split the input on the space(' ') and create an array.
* While itterating  over the array
  * I would check to see if the word was in the hash table.  If found would return the value
  * If not found I add the value to the Hash Table

Big O(time) == O(n)
Big O(size) == O(n)



## Solution
https://github.com/schoentr/data-structures-and-algorithms/blob/master/code-challanges/401/assets/repeat_word.jpg