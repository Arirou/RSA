from timeit import default_timer as timer


def exp_base(a, n, p):
    """
    fonction qui calcule les puissances succesive de a puis le modulo p de a^n
    :param a: un entier naturel
    :param n: un entier naturel
    :param p: un entier naturel
    :return: un entier naturel
    """
    return a ** n % p


def exp_mod(a, n, p):
    """
    fonction qui calcule les puissances succesive de a puis le modulo p de a^n
    :param a:un entier naturel
    :param n:un entier naturel
    :param p:un entier naturel
    :return:un entier naturel
    """
    x = a
    y = 1
    while n > 0:
        if n % 2 == 0:
            y = (y * x) % p
            n = n - 1
        else:
            x = (x * x) % p
            n = n // 2
    return y


def time(fonction):
    start = timer()
    fonction
    end = timer()
    return end - start


def lpowmod(x, y, n):
    """
    puissance modulaire:(x**y)%n
    :param x: un entier naturel
    :param y: un entier naturel
    :param n: un entier naturel
    :return: un entier naturel
    """
    result = 1
    while y > 0:
        if y & 1 > 0:
            result = (result * x) % n
        y >>= 1
        x = (x * x) % n
    return result

# print(exp_base(3,12,11))
# print(exp_base(123456,654321,789))
# print(exp_mod(3,12,11))
# print(exp_mod(123456,654321,789))
# print(lpowmod(3,12,11))
# print(time(exp_base(123456,654321,789)))
# print(time(exp_mod(123456,654321,789)))
#print(lpowmod(123456,654321,789))
