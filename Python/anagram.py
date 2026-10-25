def anagram(n1: int, n2: int) -> bool:
    n1=str(n1)
    n2=str(n2)
    if sorted(n1)==sorted(n2):
        return True
    return False

print(anagram(123,321))