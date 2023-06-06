"""

    Python getattr() function is used to access the attribute value of an object and also gives 
    an option of executing the default value in case of unavailability of the key.

    Syntax : getattr(obj, key, def)

    Parameters : 
    obj : The object whose attributes need to be processed.
    key : The attribute of object
    def : The default value that need to be printed in case attribute is not found.
    Returns : Object value if value is available, default value in case attribute is not present 
    and returns AttributeError in case attribute is not present and default value is not 
    specified. 

"""


# class GfG:
# 	name = "GeeksforGeeks"
# 	age = 24
# obj = GfG()

# print("The name is " + getattr(obj, 'name'))
# print("Description is " + getattr(obj, 'description', 'CS Portal'))
# # print("Motto is " + getattr(obj, 'motto'))



# class GfG:
# 	name = "GeeksforGeeks"
# 	age = 24

# obj = GfG()
# print("Gender is " + getattr(obj, 'gender'))




import time

class GfG:
	name = "GeeksforGeeks"
	age = 24
obj = GfG()

start_getattr = time.time()
print("The name is " + getattr(obj, 'name'))
print("The age is " + str(getattr(obj, 'age')))
print("Time to execute getattr " + str(time.time() - start_getattr))
print("The name is " + obj.name)
print("Time to execute conventional method " + str(time.time() - start_getattr))



import time

class GFG:
    name = "Nooruddin Maniyar"
    age = 29
obj = GFG()

print("My Name is " + getattr(obj, "name") + ". And My Age is " + str(getattr(obj, "age")) + ".")








class GfG:
	
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def call(self, x):
		print(f"{self.name} called with parameters '{x}'")
		return

obj = GfG("Vivek", 10)
print("obj is : ", obj)
print("GFG is : ", GfG)
print("getattr(obj, 'call') is : ", getattr(obj,'call'))

getattr(obj,'call')('arg')
