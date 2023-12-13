"""

Enumerate is a built-in function of Python. 
Its usefulness can not be summarized in a single line. 
Yet most of the newcomers and even some advanced programmers are unaware of it. 
It allows us to loop over something and have an automatic counter.

"""


# a_list = ['apple', 'banana', 'grapes', 'pear']
# for counter, value in enumerate(a_list):
#     print(counter, "-", value)
    
    
a_list = ['apple', 'banana', 'grapes', 'pear']
for counter, value in enumerate(a_list, 1):
    print(counter, "-", value)