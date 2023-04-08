def main(s):
    """
    A string of length three is given. Check that it is a palindrome.
    Return True if the palindrome is False otherwise

    Args:
        s: str
    Returns:
        bool: answer
    """
    
    return s>=0  or (s%10)==(s//10) or (s%10)==(s//100) and ((s%10)//10>=0) or (s%10)==(s//1000) and (s%100)/10==(s%1000)//100 or (s%10)==(s//10000) and (s%100)//10==(s%10000)//1000 and ((s%1000)//100)>=0
print(main(121))