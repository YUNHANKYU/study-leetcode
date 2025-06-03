# [First Try]
# Time Complexity: O(n)
# Space Complexity: O(1)
# : during the loop, check whether the previous and the next values are special values
def romanToInt1(s: str) -> int:
    value = 0
    prev = s[0]
    for i in range(len(s)):
        print(value)
        temp = prev
        prev = s[i]
        if s[i] == 'M':
            if temp == 'C':
                value += 900
            else:
                value += 1000
        elif s[i] == 'D':
            if temp == 'C':
                value += 400
            else:
                value += 500
        elif s[i] == 'C':
            if i+1 != len(s) and (s[i+1] == 'M' or s[i+1] == 'D'):
                continue
            elif temp == 'X':
                value += 90
            else:
                value += 100
        elif s[i] == 'L':
            if temp == 'X':
                value += 40
            else:
                value += 50
        elif s[i] == 'X':
            if i+1 != len(s) and (s[i+1] == 'C' or s[i+1] == 'L'):
                continue
            elif temp == 'I':
                value += 9
            else:
                value += 10
        elif s[i] == 'V':
            if temp == 'I':
                value += 4
            else:
                value += 5
        elif s[i] == 'I':
            if i+1 != len(s) and (s[i+1] == 'X' or s[i+1] == 'V'):
                continue
            else:
                value += 1
    print(value)
    return value

# [Second Try]
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# idea
# : during the loop, add the value of the current character
# : if the previous character is special character,
# : subtract two times of the value of the previous character.
#   ex) IV -> 1 + 5 - 2*1 = 4


def romanToInt2(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = roman_dict[s[0]]

    for i in range(1, len(s)):
        curr = s[i]
        prev = s[i-1]
        value += roman_dict[curr]

        # 조건문 최적화: prev를 먼저 확인
        if (prev == 'I' and (curr == 'V' or curr == 'X')) or \
           (prev == 'X' and (curr == 'L' or curr == 'C')) or \
           (prev == 'C' and (curr == 'D' or curr == 'M')):
            value -= 2 * roman_dict[prev]

    print(value)
    return value

# [LeetCode Best Try]
# Time Complexity: O(n)
# Space Complexity: O(1)
# idea
# : similar logic with [second try]
# : but it checks the next character
# : instead of the previous character


def romanToIntWhat(s: str) -> int:
    roman_hash = {"I": 1, "V": 5, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}
    n = 0
    for c in range(len(s)):
        n += roman_hash[s[c]]
        if c < len(s) - 1 and \
            ((s[c] == "I" and (s[c + 1] == "V" or s[c + 1] == "X"))
             or (s[c] == "X" and (s[c + 1] == "L" or s[c + 1] == "C"))
             or (s[c] == "C" and (s[c + 1] == "D" or s[c + 1] == "M"))):
            n -= 2 * roman_hash[s[c]]
    return n


romanToInt2("MCMXCVI")
