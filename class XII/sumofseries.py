def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def sum_of_series(x, n):
    result = sum(x**i / factorial(i) for i in range(1, n + 1))
    print(f"Sum of the series: {result}")

sum_of_series(2, 5)
