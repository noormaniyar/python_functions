"""

    function returns a map object(which is an iterator) of the results after applying
    the given function to each item of a given iterable (list, tuple etc.) 
    
    Syntax :  map(fun, iter)
    
    fun : It is a function to which map passes each element of given iterable.
    iter : It is a iterable which is to be mapped.

"""


def addition(n):
	return n + n

numbers = (1, 2, 3, 3, 4)
result = map(addition, numbers)
print(list(result))



# numbers = (1, 2, 3, 3, 4)
# result = map(lambda x: x + x, numbers)
# print(list(result))



# numbers1 = [1, 2, 3, 4, 10]
# numbers2 = [4, 5, 6, 4, 10]
# result = map(lambda x, y: x + y, numbers1, numbers2)
# print(list(result))




# l = ['sat', 'bat', 'cat', 'mat']
# test = list(map(list, l))
# print(test)




# def double_even(num):
# 	if num % 2 == 0:
# 		return num * 2
# 	else:
# 		return num

# numbers = [1, 2, 2, 3, 4, 5, 5]
# result = list(map(double_even, numbers))
# print(result)




def double_even(num):
	if num % 2 == 0:
		return num * 2
	else:
		return num

numbers = [1, 2, 3, 4, 5]
result = list(map(double_even, numbers))
print(result)




def triple(num):
    if num%2==0:
        return num*3
    else:
        return num
numbers = [1, 2, 3, 4, 5]
result = list(map(triple, numbers))
print(result)



def triplet(n):
    if not n%2==0:
        return n*3
    else:
        return n
numbers = [1, 2, 3, 4, 5]
result = list(map(triplet, numbers))
print(result)