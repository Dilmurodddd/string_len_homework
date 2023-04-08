def main(s1,s2):
    """
    Given two strings, s1 and s2. Return the shortest length between them.
    Args:
        s1: string
        s2: string
    Returns:
        shortest string
    """
    a=len(s1)
    if len(s1)>=len(s2):
        a=len(s2)
    return a
print(main('abc','abcd'))