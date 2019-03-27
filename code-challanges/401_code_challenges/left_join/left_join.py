from hashtable.hashtable import Hashtable

def left_join(ht1,ht2):
    """This function takes in two hash tables, and joins them on the keys from the first hash table.
       it returns a list of lists
    
    Arguments:
        ht1 {Hash Table}
        ht2 {Hash Table} 
    
    Returns:
        [list of lists] -- [list of lists,  [key, value from first hash table, value of second hash table]]
    """

    lst = []
    if ht1:
        for i in range (0, len(ht1._array)):
            if ht1._array[i]:
                current=ht1._array[i].head
                # import pdb; pdb.set_trace()
                while current:
                    search_key=current.value
                    # import pdb; pdb.set_trace()
                    if ht2.contains(search_key[0]):
                        lst.append([search_key[0],search_key[1],ht2.get(search_key[0])])
                    else:
                        lst.append([search_key[0],search_key[1], None])
                    
                    current=current._next
        return lst
    return 'No Hash Table Found'
            
                    
