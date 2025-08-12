# This question will take the dictionary built in count_char_n_grams() as an argument
# to calculate the possibilities for the next letter given the previous n-1 letters 
# (from the prompt string).
# You can assume that the parameter prompt has length n-1, and counts has the format of the map output by count_char_n_grams().

def next_letter_frequency(prompt: str, counts: dict[str, int]) -> dict[str, int]:
    # Return a dictionary where the keys are the options for the nth character (given
    # the previous n-1 characters), and the values are the number of times that that
    # character is the nth character in the counts.
    # For example, in the string "Rasika has a cat. Ellen has a cat. Miguel has a dog."
    # with n=4, we know that count_char_n_grams() should have included that " a c"
    # appears twice and " a d" appears once. So, next_letter_frequency(" a ", counts)
    # should return the dictionary {c: 2, d: 1} because, out of all the times that
    # " a *" appears, * is c twice and * is d once.
    pass
