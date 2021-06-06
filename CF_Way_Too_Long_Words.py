# A. Way Too Long Words
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Sometimes some words like "localization" or "internationalization" are so long that writing them many times in one text is quite tiresome.

# Let's consider a word too long, if its length is strictly more than 10 characters. All too long words should be replaced with a special abbreviation.

# This abbreviation is made like this: we write down the first and the last letter of a word and between them we write the number of letters between the first and the last letters. That number is in decimal system and doesn't contain any leading zeroes.

# Thus, "localization" will be spelt as "l10n", and "internationalization» will be spelt as "i18n".

# You are suggested to automatize the process of changing the words with abbreviations. At that all too long words should be replaced by the abbreviation and the words that are not too long should not undergo any changes.

# Input
# The first line contains an integer n (1 ≤ n ≤ 100). Each of the following n lines contains one word. All the words consist of lowercase Latin letters and possess the lengths of from 1 to 100 characters.

# Output
# Print n lines. The i-th line should contain the result of replacing of the i-th word from the input data.

# Examples
# inputCopy
# 4
# word
# localization
# internationalization
# pneumonoultramicroscopicsilicovolcanoconiosis
# outputCopy
# word
# l10n
# i18n
# p43s

# Explanation:
# If the alphabets in the word are more than 10 then we need to print the abbreviation of the word.
# If the alphabets in the word are less than 10 then we simply need to print the letter as it is.
# To print the abbreviation of the word we need to print the first word, the length of word - 2 and the last alphabet
# For output we need to take the word as input and print the word or the abbreviation as per the condition one by one.

limit = int(input())
for word in range(limit):
    word = input()
    if len(word) > 10:
        print(word[0], end = "")
        print(len(word) - 2, end = "")
        print(word[-1])
    else:
        print(word)