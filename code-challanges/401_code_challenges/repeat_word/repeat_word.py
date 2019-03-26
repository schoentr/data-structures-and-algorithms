from hashtable.hashtable import Hashtable

def repeat_word(long_string):
    start=0
    word=''
    words_ht = Hashtable()
    long_string = long_string.lower()
    words= long_string.split(' ')
    for word in words:
        if words_ht.contains(word):
            return word
        else:
            word_hash = words_ht.hash(word)
            words_ht.add(word,word_hash)
    return 'No matching Words'
         

    