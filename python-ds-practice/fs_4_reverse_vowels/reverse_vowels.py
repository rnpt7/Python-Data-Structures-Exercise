def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in the string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = []

    for char in s:
        if char in "aeiouAEIOU":
            vowels.append(char)

    vowels = vowels[::-1]
    cnt = 0
    result = ""

    for char in s:
        if char in "aeiouAEIOU":
            result += vowels[cnt]
            cnt += 1
        else:
            result += char
            
    return result

