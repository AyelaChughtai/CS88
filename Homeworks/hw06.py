## Debug This
def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2  * 0
    0
    """
    if n == 0:
        return 0
    else:
        return n * skip_mul(n - 2)


## MapReduce
def map(f, s):
    """
    Map a function f onto a sequence.

    >>> def double(x):
    ...     return x * 2
    >>> def square(x):
    ...     return x ** 2
    >>> def toLetter(x):
    ...     alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ...     return alpha[x%26]
    >>> map(double, [1,2,3,4])
    [2, 4, 6, 8]
    >>> map(square, [1, 2, 3, 4, 5, 10])
    [1, 4, 9, 16, 25, 100]
    >>> map(toLetter, [3, 0, 19, 0])
    ['d', 'a', 't', 'a']

    """
    if s == []:
        return s
    return [f(s[0])] + map(f, s[1:])


def filter(f, s):
    """Filter a sequence to only contain values allowed by filter.

    >>> def is_even(x):
    ...     return x % 2 == 0
    >>> def divisible_by5(x):
    ...     return x % 5 == 0
    >>> filter(is_even, [1,2,3,4])
    [2, 4]
    >>> filter(divisible_by5, [1, 4, 9, 16, 25, 100])
    [25, 100]
    """
    if s == []:
        return []
    if f(s[0])==True:
        return [s[0]] + filter(f, s[1:])
    else:
        return filter(f, s[1:])


from operator import add, mul

def reduce(reducer, s, base):
    """Reduce a sequence under a two-argument function starting from a base value.

    >>> def add(x, y):
    ...     return x + y
    >>> def mul(x, y):
    ...     return x*y
    >>> reduce(add, [1,2,3,4], 0)
    10
    >>> reduce(mul, [1,2,3,4], 0)
    0
    >>> reduce(mul, [1,2,3,4], 1)
    24
    """
    if s == []:
        return base
    else:
        return reduce(reducer, s[1:], reducer(s[0], base))


# Recursive Math

def summation(n, term):
    """Return the sum of the 0th to nth terms in the sequence defined
    by term.
    Should be implemented using recursion.

    >>> summation(5, lambda x: x * x * x)
    225
    >>> summation(9, lambda x: x + 1)
    55
    >>> summation(5, lambda x: 2**x)
    63
    """
    # total, k = 0, 1
    # while k <= n:
    #        total, k = total + term(k), k + 1
    #    return total

    if n<1:
        return term(n)
    return term(n)+summation(n-1, term)


def count_digit(n, digit):
    """Return how many times digit appears in n.

    >>> count_digit(55055, 5)
    4
    >>> count_digit(1231421, 1)
    3
    >>> count_digit(12, 3)
    0
    """ 
    if n<10:
        if digit==n:
            return 1
        else:
            return 0
    elif digit == (n%10):
        return 1 + count_digit(n//10, digit)
    else:
        return 0 + count_digit(n//10, digit)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """
    if n < 10:
        return 0
    else:
        return ten_pairs(n//10) + count_digit(n//10, 10 - n%10)

