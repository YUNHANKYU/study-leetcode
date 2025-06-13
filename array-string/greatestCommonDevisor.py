def gcdOfStrings(str1: str, str2: str) -> str:
    # str1 와 str2 의 길이의 GCD 를 구하면
    # 그 길이의 prefix 문자열이 str1과 str2의 공약 문자열이 될 수 있다.
    # 그 전에 두 문자열이 GCD 문자열로 이루어져있는지 확인해야한다.
    # str1 + str2 == str2 + str1 인지 확인한다.

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    gcd_len = gcd(len(str1), len(str2))

    if str1 + str2 != str2 + str1:
        return ''

    print(str1[:gcd_len])
    return str1[:gcd_len] if str1[:gcd_len] == str2[:gcd_len] else ''


gcdOfStrings('ABABAB', 'ABAB')
