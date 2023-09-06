# Every positive fraction can be represented as sum of unique unit fractions. 
# A fraction is unit fraction if numerator is 1 and denominator is a positive integer, 
# for example 1/3 is a unit fraction. Such a representation is called Egyptian Fraction as it was used by ancient Egyptians. 

# Following are a few examples: 

# Egyptian Fraction Representation of 2/3 is 1/2 + 1/6
# Egyptian Fraction Representation of 6/14 is 1/3 + 1/11 + 1/231
# Egyptian Fraction Representation of 12/13 is 1/2 + 1/3 + 1/12 + 1/156

import math
 
def egyptianFraction(nr, dr):
 
    print("The Egyptian Fraction " +
          "Representation of {0}/{1} is".
                format(nr, dr), end="\n")
 
    # empty list ef to store
    # denominator
    ef = []
 
    # while loop runs until
    # fraction becomes 0 i.e,
    # numerator becomes 0
    while nr != 0:
 
        # taking ceiling
        x = math.ceil(dr / nr)
 
        # storing value in ef list
        ef.append(x)
 
        # updating new nr and dr
        nr = x * nr - dr
        dr = dr * x
 
    # printing the values
    for i in range(len(ef)):
        if i != len(ef) - 1:
            print(" 1/{0} +" .
                    format(ef[i]), end = " ")
        else:
            print(" 1/{0}" .
                    format(ef[i]), end = " ")
 
# calling the function
egyptianFraction(6, 14)