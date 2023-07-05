"""The filter_anagrams() function returns a list whose
elements are words from the list 'words' that represent
an anagram of the 'word' word. If the words list is empty
or contains no anagrams, the function returns an empty list."""


def filter_anagrams(word: str, words: list) -> list:
    arr = []
    for i in range(len(words)):
        if sorted(list(word)) == sorted(list(words[i])):
            arr.append(words[i])

    return arr