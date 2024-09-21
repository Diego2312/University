#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Your dear friend Pico de Paperis sent you a very strange message scribbled on a postcard.
You haven't seen him in a long time and you've always had fun writing to each other in code.
To decode his message, go and look for a rather particular book in your library,
the Archimedes Pythagorean cipher. The cipher to be applied is the famous "Pharaoh's Cipher".
The decipherment with the Pharaoh's method is based on rules for substituting sequences of symbols in the text.
The reason why it is called "Pharaoh's cipher" is that in ancient Egyptian sequences made up of multiple hieroglyphs
could be written in any order, so any anagram of the sequences was valid.
To make things stranger, Pico de Paperis decided to use a cipher that is not exactly the one of Pharaoh,
but a variant of it. Instead of using anagrams he uses "quasi-anagrams", that is, anagrams that in the original text
have one more spurious character than the searched sequence.
The cipher contains pairs of sequences that indicate how to transform the text.
For example, the pair 'shampoo' -> 'soap' corresponds to searching for a point in the message where the sequence
'shampoo' appears (or an anagram of it) but with an extra character (e.g. 'pmQohaso')
and replace it with the sequence 'soap'.
Decoding the message can lead to more possible final messages, because there can be more sequences in the text
that can be transformed at any time and the order of transformations influences subsequent transformations.
At some point it will happen that none of the "quasi-anagrams" of a cipher sequence is present anywhere
in the sequence of symbols, and therefore it is no longer possible to make transformations.
We call these sequences final sequences.
Of all the possible final sequences, the one we are interested are all the shortest.

To decode the Pico de Paperis message you must implement the function
pharaohs_revenge(encrypted_text : str, pharaohs_cypher : dict[str,str]) -> set[str]:
which receives as arguments:
- the text that Pico de Paperis sent you, as a string of symbols (characters)
- the cipher to be applied, a dictionary whose keys are the sequences to search for a quasi-anagram in the text
    and as the associated value the string to replace the quasi-anagram found with.
The function must return the set of the shortest texts obtainable by repeatedly applying
the transformations until it is no longer possible to apply any of them.

Example:
encrypted_text  = 'astronaut-flying-cyrcus'
pharaohs_cypher = {'tuar': 'me', 'cniy': 'op', 'sorta': 'tur', 'fult': 'at', 'rycg': 'nc'}

Result: {'tmeopcus', 'metopcus', 'ameopcus', 'atmepcus'}
Notice, and all the transformations applied are those contained in the example.txt file
(in alphabetical order and without repetitions)

NOTE: At least one of the functions or methods you implement must be recursive
NOTE: the recursive function/method must be defined at the outermost level
      otherwise you will fail the recursion test.
'''

from tree import Tree


def new_tracker(sequence, key_srt, seq_len):
    srt_sequence = sorted(sequence) #sort the sequence to compare same indexes
    j = 0 
    check = False #Iniatialize a checker that keeps track if a comparison is different
    for element in range(seq_len):
        if srt_sequence[element] == key_srt[j]: #compare
            j+= 1 #iteration continues for the key only if the comparison is true
            continue
        else:
            if check == False: #if the comparison is not true, the checker becomes True (meaning a comparison was different.)
                check = True
            else:
                return False #if the checker is True, this means a different comparison was already found, exceeding the 1 extra character for quasi-anagrams
    
    if srt_sequence[-1] == key_srt[-1]: #handle the last character of the sequence
        return True
    elif check == True:
        return False
    return True
            
        

def check_quasi_anagrams(sequence, encrypted_text : list(), len_dict, len_text): 
    srt_sequence = sorted(sequence) #def a sorted variable to use in tracker
    quasi = []
    seq_len = len(sequence)
    #Take every tamanho + 1 comb sequence. (every possible quasi-anagram)
    for i in range(len(encrypted_text) - len_dict[sequence]): #The range goes from zero to the last sequence of the text, so len(text) - len(sequence)

        pos_seq = encrypted_text[i:i+len_dict[sequence]+1] #Set possible sequence. Goes from current character to the len(sequence) + 1, because quasi anagram
        
        if new_tracker(pos_seq, srt_sequence, seq_len): #Check if the sequence is a quasi
            quasi.append(pos_seq)
    return quasi





def str_tree(tree, text, pharaohs_cypher : dict[str,str], leafs, len_dict): #create the tree with all changes until, none are possible
    len_text = len(text)
    
    for i in pharaohs_cypher:
        pos_quasi = check_quasi_anagrams(i, text, len_dict, len_text) #get all possible quasi for all keys in the dict
        if pos_quasi != []: #check if there were quasis

            for j in pos_quasi: #for every quasi
            
                new_text = text.replace(j, pharaohs_cypher[i]) #replace the quasi with it's corresponding value in current text  
                
                new_tree = Tree(new_text) #create a new tree for the replaced text
                
                tree.children.append(new_tree) #append to the current tree, the new one
                
                str_tree(new_tree, new_text, pharaohs_cypher, leafs, len_dict) #call the function again for the new text and new tree (recursive)
                                            
                if new_tree.isLeaf() and new_text not in leafs: #get all leaves
                    leafs.append(new_text)

    return tree
            

    

def pharaohs_revenge(encrypted_text : str, pharaohs_cypher : dict[str,str]) -> set[str]:
    
    #Variables to pass in to function
    
    head_Tree = Tree(encrypted_text)    
    leafs = []    
    len_dict = {i:len(i) for i in pharaohs_cypher}
      
    str_tree(head_Tree, encrypted_text, pharaohs_cypher, leafs, len_dict)
    
    #Handle the function output to fit desired format
    srt_leafs = sorted(leafs, key=lambda x:len(x))
    find_len = len(srt_leafs[0])
    
    final_set = set(([i for i in srt_leafs if len(i) == find_len]))
    
    
        
    return final_set

encrypted_text =  "aaabaaac"
pharaohs_cypher = {"aa":"bc","bb":"c","cc":"d"}
if __name__ == '__main__':
    print(pharaohs_revenge(encrypted_text, pharaohs_cypher))
    
    
    
"""
What to do :
    
    Return a set of the shortest final sequences of the input encrypted text, using the pharaohs_sypher to decrypt it.
    
    
Image this problem as a tree. The head of the tree is the encrypted string. From the this head, various changes can be made based on which quasi-anagram
from the cypher is present in it. For every possible change, we have a branch. And for every branch we can create new ones, until finally there are no more
changes that can be done. From all these changes I must return the ones with the shortest lengths.

The main idea of the tree is to, through a for loop, add a child if the key is present in the string with the value of the replaced string. This process will 
happen recursively, creating all possible branches of changes, resulting in many leafs (final sequences to be analysed).

I need to find a way to check if a quasi-anagram of a key is present in a string. A process that works for any key and any string.

To check if the quasi-anagram is present, I can simply use the 'in' fucntion, since order does not matter.

I need to make this a recursive process

I need to find a way to access
    

Is it possible to have more than one quasi-anagram
"""