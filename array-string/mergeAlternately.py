def mergeAlternately(word1: str, word2: str) -> str:
    # word1과 word2를 번갈아가며 합친 문자열을 반환한다.
    # word1과 word2의 길이가 다르면, 남은 문자열을 합친다.
    # 두 개의 포인터를 운용하며 번갈아가면서 문자열을 합친다.
    merged = ''
    isWord1 = True
    index = 0
    for i in range(len(word1)):
        merged += word1[i]
        merged += word2[i]
        if i+1 == len(word1):
            index = i+1
            break
        elif i+1 == len(word2):
            isWord1 = False
            index = i+1
            break
    merged += (word2[index:] if isWord1 else word1[index:])
    print(merged)
    return merged


mergeAlternately('abc', 'pqr')
