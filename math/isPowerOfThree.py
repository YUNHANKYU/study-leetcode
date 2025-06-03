def isPowerOfThree(n: int) -> bool:
    if n == 1:
        return True
    if n < 3 or n % 3 != 0:
        return False

    while n % 3 == 0:
        n //= 3

    print(n == 1)
    return n == 1


def isPowerOfThreeEasy(n: int) -> bool:
    return n > 0 and 3**20 % n == 0


print(isPowerOfThreeEasy(25))
