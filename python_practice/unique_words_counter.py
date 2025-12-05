#This script counts the number of different words in a sentence 

def count_unique_words(sentence: str) -> int: 

    """ This function will take a string as a parameter and output an integer.
     
      Args:
       
        Parameter 1 (string): the sentence from the user that we want to count the unique words 
         
      Returns: 
       
        integer: the number of unique words within the sentence """

    #first we must split the sentence into a list of words, otherwise we'll get a set of different characters
    #then we can safely convert it to a set, because of how the algorithm works, sets automatically exclude duplicates!
    set_of_words = set(sentence.split()) #the method split() returns a list by itself.

    unique_words_number = len(set_of_words) #len function returns the total number of elements within a data structure.

    print(unique_words_number)

    return unique_words_number


#input method almost never throws exception, so this might be redundant here, but still this is good coding practice so we'll add it anyways 
try:

    unique_word = input("Please enter a sentence to count its unique words: ").lower() #input function always returns a string 
    count_unique_words(unique_word)

except Exception as e:

    print(f"An unexpected error occurred: {e}")




