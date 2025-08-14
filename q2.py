"""
When we process text in machine learning, we often use character ngrams instead of entire words, to avoid dealing with punctuation and typos.
For example, the text "Rasika", with a value of n=4, has these character ngrams: "Rasi", "asik", and "sika".
Each of these character ngrams appears once in "Rasika", and each of them appears twice in "RasikaRasika"
(and "RasikaRasika" also has the additional character ngrams "ikaR", "kaRa", and "aRas", each of which appears once).

Please implement count_char_n_grams() below according to the comments describing its functionality.
You will need to write the documentation.
"""

def count_char_n_grams(text: str, n: int = 3) -> dict[str, int]:
    # Very similar to count_words(), but instead of counting entire words, it counts each sequence of n characters.
    # The main difference will be that instead of splitting the text using a space, you will iterate through the
    # characters of the String and use the appropriate indices to build substrings which are character ngrams.
    # Note the default value of the parameter n.
    pass
