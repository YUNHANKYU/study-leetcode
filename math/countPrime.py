# [logic]
# 1. loop from 2~n
# 2. check if the list's value is 0
# 3. if it's 0, change all the multiple of the number to 1
# 4. count the number of 0

def countPrimes(n: int) -> int:
    count = 0
    check_list = [0] * n

    for i in range(2, n):
        if check_list[i] == 0:
            for j in range(i, n, i):
                check_list[j] = 1
            count += 1

    print(count)
    return count


countPrimes(1000)
