def factorial_literaive(n):
    result = 1
    # 1 부터 n 까지의 수를 차례대로 곱하기
    for i in range (1, n+1):
        result *= i

    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    # n! = n*(n-1)!를 그대로 코드로 작성하기
    return n * factorial_recursive(n-1)


print('반복적으로 구현:', factorial_literaive(5))
print('재귀적으로 구현:', factorial_recursive(5))