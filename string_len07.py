def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    a=''
    # a=len(s1)
    # b=len(s2)
    # c=len(s3)
    if (len(str(s1))+1)%2==0:
        a=s1
    if (len(str(s2))+1)%2==0:
        a=str(a)+s2
    if (len(str(s3))+1)%2==0:
        a=str(a)+s3
    return a
print(main('a','ab','abc'))
