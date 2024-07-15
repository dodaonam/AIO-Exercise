def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def sin_x(x, n):
    result = 0
    if n <= 0:
        return
    for i in range(n):
        temp = (-1)**i * (x**(2*i + 1)) / factorial(2*i + 1)
        result += temp
    return result


def cos_x(x, n):
    result = 0
    if n <= 0:
        return
    for i in range(n):
        temp = (-1)**i * (x**(2*i)) / factorial(2*i)
        result += temp
    return result


def sinh_x(x, n):
    result = 0
    if n <= 0:
        return
    for i in range(n):
        temp = (x**(2*i + 1)) / factorial(2*i + 1)
        result += temp
    return result


def cosh_x(x, n):
    result = 0
    if n <= 0:
        return
    for i in range(n):
        temp = (x**(2*i)) / factorial(2*i)
        result += temp
    return result


print(sin_x(3.14, 10))
print(cos_x(3.14, 10))
print(sinh_x(3.14, 10))
print(cosh_x(3.14, 10))