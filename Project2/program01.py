#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consider the positional encoding of a number in base B.  Given the N
digits: a_{N-1} .... a_1 a_0 The value of the number is obtained by
summing, for each index i from 0 to N-1, the values a_i*B^i.

Example: if the base B=6 and the number is (52103)_6
Its value will be 5*6^4 + 2*6^3 + 1*6^2 + 0*6^1 + 3*6^0 = (6951)_10

Let's generalize this notation to use different bases for each
position: we will have a list "bases" consisting of N bases and a
number consisting of N digits contained in a list named "digits."  For
the example above, we will have: bases = [6, 6, 6, 6, 6], digits = [5,
2, 1, 0, 3]. The digits are such that each digit is less than the base
in the same position. The value of the number in base 10 is obtained
as in the initial conversion, using the i-th base from the list for
the i-th power.

NOTE: For convenience, we will use lists of digits and bases in which
the exponent of the power corresponds to the index in the lists. So,
each list will contain bases and digits starting from the units.

NOTE: The number of bases N is strictly greater than 1. The values of
the bases are also greater than 1.

Based on what has been said, one input for the homework is to generate
a list of all possible valid combinations of digits representable with
those bases.

Example: if the input bases are [2, 5], all combinations are:
[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]

In fact:
- In the first digit, there are only values between [0, 1] because the base is 2.
- In the second digit, there are only values between [0, 4] because the base is 5.

Each combination represents an integer that needs to be converted from
a list to an integer according to the base specified in "bases." Once
all possible combinations have been converted into integers, it is
necessary to find which integers have more than one representation in
the given bases.

Example: If the input bases are [4, 3, 2], then the integers that
admit more than one representation are {3, 4, 5, 6, 7, 8, 9, 10}

In fact, for example, the number 10 with these bases has two representations:
[3, 1, 1] -> 3*4^0 + 1*3^1 + 1*2^2 = 10
[0, 2, 1] -> 0*4^0 + 2*3^1 + 1*2^2 = 10

The problem has already been divided into subproblems, and you need to
implement the following functions:
 - decode_digits is the simplest and fundamental function that
   receives a list of bases and a list of digits and converts it into
   an integer.
 - generate_digits is the function that does most of the work, given a
   list of bases, it calculates all combinations.
- find_doubles is the final function that, given the combinations,
  finds the corresponding integers that have more than one
  representation.

Each test must be completed within a timeout of 0.5 seconds.

ATTENTION: Importing libraries other than those already present is prohibited.
"""

from typing import List, Set


def decode_digits(digits: List[int], bases: List[int]) -> int:
    '''
    Receives a list of digits and a list of bases of the same length.
    Calculates the integer value as explained earlier.
    Parameters
    digits : List[int]    list of digits to convert
    bases   : List[int]    list of bases of the same length
    Returns
    int                    the corresponding integer value
    
    Example: decode_digits( [1, 1, 2], [2, 3, 4] ) -> 36
    in fact, 1*2^0 + 1*3^1 + 2*4^2 = 36
    '''


    num = 0
    for i in range(len(digits)):
        num += digits[i]*bases[i]**i #Calculates the value of each digit and adds to num
    return num

"""
I have two lists as input and an integer as ouput. I need to create the "rule of creation" for the integer. 
To get the integer i must use the digits and their respective bases. 
Both lists have equal lengths, and the base for each digit is at the same index of the base list.
"""


def generate_digits(bases : List[int] ) -> List[List[int]]:
    '''
    Given a list of bases, generates a list of all possible
    combinations of digits compatible with the given bases. Each
    combination is a list of compatible digits. Specifically, for
    each position corresponding to a base B, it contains one of the
    possible digits in [0..B-1].

    Example: generate_digits([2, 5]) produces the list
    [ [0, 0], [1, 0], [0, 1], [1, 1], [0, 2], [1, 2], [0, 3], [1, 3], [0, 4], [1, 4] ]

    Note: The order in the final list does not matter, and even
    [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]
    is a valid solution.
    '''

    #Initialize 2 lists that will be used to store the combinations
    all_combinations = []
    first_comb =[]


    #Get the initial combination
    for z in range(len(bases)):
        first_comb.append(0)


    #How many possible combinations
    combs = 1
    for i in bases:
        combs *= i


    #Calculate only once the law of change for each index
    every_n = []
    for x in range(len(bases)):
        ind = 1
        for y in bases[x:]:
            ind *= y
            end = combs/ind
        every_n.append(end)


    counter = 1 #To keep track of current iteration

    #Main loop

    for i in range(combs):

        #iterate through each digit
        for j in range(len(bases)):
            if counter % every_n[j] == 0: # Check if it is time to add one to the digit
                first_comb[j] += 1
                if first_comb[j] == bases[j]: #When the digit reaches n, it goes to zero (since the last digit must be n-1)
                    first_comb[j] = 0

        counter += 1 #Keep up with iterations

        all_combinations.append(first_comb.copy()) #Append each new combination to a list that will contain all combinations

    return all_combinations


def find_doubles(bases : List[int]) -> Set[int]:
    '''
    Given a list of bases, generates a list of all possible valid
    combinations of digits representable with those bases, converts
    each combination into the corresponding integer, and looks for
    integers that appear more than once.

    Returns the set of integer values that have more than one
    representation in the given bases.

    Example: find_doubles([4, 3, 2]) -> {3, 4, 5, 6, 7, 8, 9, 10}
    In fact, for example, the number 10 with these bases has two representations:
    [3, 1, 1] -> 3*4^0 + 1*3^1 + 1*2^2 = 10
    [0, 2, 1] -> 0*4^0 + 2*3^1 + 1*2^2 = 10
    '''


    all_combs = generate_digits(bases) #Generate all possible combinations

    all_ints = [] #Intialize list with all possible ints
    final_ints = set() #Initialize set with all double ints

    #Get all possible ints
    for i in all_combs:
        all_ints.append(decode_digits(i, bases))

    #Find every int that repeats itself
    for j in range(len(all_ints)):
        if all_ints[j] in all_ints[j+1:]:
            final_ints.add(all_ints[j])
    return final_ints
    pass


###################################################################################
if __name__ == '__main__':

    test_list = [2, 2, 2, 2, 2]

    #print(decode_digits([1, 1, 2], [2, 3, 4]))
    print(generate_digits(test_list))
    #print(find_doubles(test_list))

    # Enter your tests here
    # If you want to test your code on small data
    # Note that to run this main, you should use program.py
    # as a client and not as a module, meaning with 'python program.py'
    pass

