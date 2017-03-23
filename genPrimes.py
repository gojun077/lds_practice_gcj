def genPrimes():
    """
    Generator function that returns the next prime number each
    time it is called. Previously generated primes will be memoized
    inside of a list 'p'.  A prime is a natural number greater than 1
    that has no positive divisors other than 1 and itself. The first
    prime is '2'.

    A candidate number x is prime if (x % p) != 0 for all earlier
    primes p.

    """
    yield 2
    yield 3
    p = [2, 3]
    x = p[-1]

    while True:
        x += 2
        for i in p:
            if (x % i) == 0:
                break
        else:  # if no break in for-loop
            p.append(x)
            yield x

# ipython에서 아래와 같이 테스트 하세요:
#foo = genPrimes()
# foo.__next__()
#>>> 2
# foo.__next__()
#>>> 3
#...
