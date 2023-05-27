"""

    A Lambda function is a small Anonymous function.

    A Lambda function can take any number of arguments, but can only have single expression.
    Use lambda functions when an anonymous function is required for a short period of time.

    lambda arguments : expression

"""

x = lambda a : a + 10
print(x(5))


# x = lambda a, b : a * b
# print(x(5, 6))


# x = lambda a, b, c, d : a + b + c + d
# print(x(5, 8, 7, 9))


# q = 10
# x = lambda a : a * (5 if q>1 else False)
# print(x(2))


# def myfunction(n):
#     return lambda a : a * n

# mydoubler = myfunction(2)
# print(mydoubler(10))


# mytripler = myfunction(3)
# print(mytripler(111))

