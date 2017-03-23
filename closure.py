def general_poly(L):
    """
    list -> integer

    Calculate the digit sum of a number whose digits are stored
    in a List of Integers

    >>> general_poly([1, 2, 3, 4])(10)
    1234

    >>> general_poly([0, 0, 2, 0])(1)
    2
    """
    def apply_base(x):
        max_degree = len(L) - 1
        ans = 0

        for i in L:
            ans += i * x**max_degree
            max_degree -= 1
        return ans
    return apply_base
