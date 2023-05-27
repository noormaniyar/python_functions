"""

    The Filter function returns an iterator , where the items are filtered through a function
    to test if the item is accepted or not.

    syntax :  filter(function, iterable)

"""


ages = (12, 26, 34, 26, 16, 65, 43, 45, 87, 15, 15)

def myfunction(age):
    if age > 18:
        return True
    else:
        return False

adults_list = list(filter(myfunction, ages))
print(adults_list)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def check_even(number):
#     if number % 2 == 0:
#         return True  
#     else:
#         return False

# even_numbers = list(filter(check_even, numbers))
# print(even_numbers)



# alphabets_list = ['a', 'b', 'd', 'e', 'f', 'h', 'i', 'm', 'n', 'o', 't', 'u', 'v', 'x']

# def check_vowels(alphabet):
#     if alphabet in ['a', 'e', 'i', 'o', 'u', 'v']:
#         return True
#     else:
#         return False

# print(tuple(filter(check_vowels, alphabets_list)))    # Do print either list or tuple in single time
# # print(list(filter(check_vowels, alphabets_list)))



# numbers = [1,2,3,4,5,6,7,8,9,10]

# # solution 1 
# even_numbers = filter(lambda number : (number % 2 == 0), numbers)
# print(list(even_numbers))

# # solution 2
# def even_calculator(number):
#     if number % 2 == 0:
#         return True  
#     else:
#         return False
# even_numbers = filter(even_calculator, numbers)
# print(list(even_numbers))




# random_list = ['a', 0, 1, False, True, 0, '0', 'o']
# filtered_iterator = filter(None, random_list)
# print(list(filtered_iterator))    #filter function not return (False, 0) values




# alphabets_list = ['a', 'b', 'c', 'f', 'd', 'e', 'h', 'f', 'g', 'h', 'u', 'i', 'o', 'p', 'a', 'e', 'n', 'v', 'l']
# vowels_list = ['a', 'e', 'i', 'o', 'u', 'v']

# #solution 1
# def check_non_vowels(alphabet):
#     if alphabet in vowels_list:
#         return False
#     else:
#         return True
# #solution 2
# def check_non_vowels(alphabet):
#     if alphabet not in vowels_list:
#         return True
#     else:
#         return False

# print(list(filter(check_non_vowels, alphabets_list)))



# num_list = [1, 2, 3, 3, 4, 5, 6, 7, 8, 8, 9, 10]

# even_list = filter(lambda x : (x if x % 2 == 0 else False), num_list)
# print(list(even_list))

# odd_list = filter(lambda x : (x if x%2 !=0 else False), num_list)
# print(list(odd_list))




# str_list = ['a', 'rrr', 'bt', 't', 'ttt', 'qw', 'sd', 'ed', 't', 'v']
# parameter = 't'

# def parameter_checker(str):
#     if not str in parameter:
#         return True
#     else:
#         return False

# print(list(filter(parameter_checker, str_list)))




# str_list = ['a', 'rrr', 'bt', 't', 'ttt', 'qw', 'sd', 'ed', 't', 'v']
# parameter = 't'

# res = filter(lambda x : (x if x!=parameter else ""), str_list)
# print(list(res))

# res = filter(lambda x : (x if parameter in x else False), str_list)
# print(list(res))


# res = filter(lambda x : (x if not parameter in x else False), str_list)
# print(list(res))




















