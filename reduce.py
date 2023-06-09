"""

    The reduce(fun,seq) function is used to apply a particular function passed in its argument
    to all of the list elements mentioned in the sequence passed along.
    This function is defined in “functools” module.

    Working :  

    At first step, first two elements of sequence are picked and the result is obtained.
    Next step is to apply the same function to the previously attained result and the number 
    just succeeding the second element and the result is again stored.
    This process continues till no more elements are left in the container.
    The final returned result is returned and printed on console.

"""

# import functools

# lis = [1, 3, 5, 6, 2]

# res = functools.reduce(lambda a, b: a+b, lis)
# print("The sum of the list elements is : ", res)

# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))





import functools
import operator

lis = [1, 3, 5, 6, 2]

print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))

print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))

res = functools.reduce(operator.add, ["geeks", "for", "geeks"])
print("The concatenated product is : ", res)
