def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?
    
        >>> single_letter_count('Hello World', 'h')
        1
        
        >>> single_letter_count('Hello World', 'z')
        0
        
        >>> single_letter_count("Hello World", 'l')
        3
    """ 
    cnt = 0
    word = word.lower()
    letter = letter.lower()
    for char in word:
        if char == letter:
            cnt += 1
    return cnt