def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    
    k=0
    if (len(s)+1)%2==0:
        k=s[(len(s)%2)]
    if (len(s))%2==0:
        k=f'{s[((len(s)//2)-1)]}{s[(len(s)//2)]}'
        # k=f"{main[a]}{main[b]}"
    return k
print(main('bcd'))