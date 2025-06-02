def fizzBuzz(n: int) -> list[str]:
    # 1. n만큼 반복하면서
    # 2. 그 수가 15 의 배수면 'FizzBuzz'
    # 3. 그 수가 3 의 배수면 'Fizz'
    # 4. 그 수가 5 의 배수면 'Buzz'
    result = []
    for i in range(1, n+1):
        if i % 15 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(str(i))

    print(result)
    return result


fizzBuzz(25)
