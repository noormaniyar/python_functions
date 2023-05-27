"""

The Filter function returns an iterator , where the items are filtered through a function to test if the item is accepted or not.

syntax :  filter(function, iterable)

"""


ages = [12, 34, 16, 65, 43, 45, 87, 15]

def myfunction(x):
    if x > 18:
        return True
    else:
        return False

adults = filter(myfunction, ages)

adults_list = list(adults)
print(adults_list)

# for i in adults:
#     print(i)



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def check_even(number):
    if number % 2 == 0:
        return True  
    else:
        return False

even_numbers_iterator = filter(check_even, numbers)

even_numbers = list(even_numbers_iterator)

print(even_numbers)



alphabets_list = ['a', 'b', 'd', 'e', 'f', 'h', 'i', 'm', 'n', 'o', 't', 'u', 'v', 'x']

def check_vowels(alphabets_list):
    if alphabets_list in ['a', 'e', 'i', 'o', 'u', 'v']:
        return True
    else:
        return False

vowels = filter(check_vowels, alphabets_list)

print(tuple(vowels))    # Do print either list or tuple in single time
# print(list(vowels))



numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = filter(lambda x : (x % 2 == 0), numbers)
print(list(even_numbers))



random_list = ['a', 0, 1, False, True, 0, '0', 'o']

filtered_iterator = filter(None, random_list)
print(list(filtered_iterator))




alphabets_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'u', 'i', 'o', 'p', 'a', 'e', 'n', 'v', 'l']
vowels_list = ['a', 'e', 'i', 'o', 'u', 'v']

def check_non_vowels(alphabets_list):
    if alphabets_list in vowels_list:
        return False
    else:
        return True

print(list(filter(check_non_vowels, alphabets_list)))



num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = filter(lambda x : (x if x % 2 == 0 else False), num_list)
print(list(even_list))

odd_list = filter(lambda x : (x if x%2 !=0 else False), num_list)
print(list(odd_list))




str_list = ['a', 'rrr', 'b', 't', 'ttt', 'qw', 'sd', 'ed', 'v']
parameter = 't'

def parameter_checker(str_list):
    if not str_list in parameter:
        return True
    else:
        return False

print(list(filter(parameter_checker, str_list)))




str_list = ['a', 'rrr', 'b', 't', 'ttt', 'qw', 'sd', 'ed', 'v']
parameter = 't'

res = filter(lambda x : (x if x!=parameter else ""), str_list)
print(list(res))

res = filter(lambda x : (x if parameter in x else False), str_list)
print(list(res))


res = filter(lambda x : (x if not parameter in x else False), str_list)
print(list(res))




















