"""

    zip() method takes iterable containers and returns a single iterator object, 
    having mapped values from all the containers. 

    It is used to map the similar index of multiple containers so that they can be used 
    just using a single entity. 

    Syntax :  zip(*iterators) 

    Parameters : Python iterables or containers ( list, string etc ) 
    Return Value : Returns a single iterator object.

"""



name = [ "Manjeet", "Nikhil", "Shambhavi", "Astha" ]
roll_no = [ 4, 1, 3, 2 ]
mapped = zip(name, roll_no)
print(set(mapped))


names = ['Mukesh', 'Roni', 'Chari']
ages = [24, 50, 18]

for i, (name, age) in enumerate(zip(names, ages)):
	print(i, name, age)



stocks = ['GEEKS', 'For', 'geeks']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}
print(new_dict)



tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped = zip(tuple1, tuple2)
print(list(zipped))



list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['x', 'y', 'z']
zipped = zip(list1, list2, list3)
result = list(zipped)
print(result)





name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]


mapped = zip(name, roll_no, marks)
mapped = list(mapped)
print("The zipped result is : ", mapped)


namz, roll_noz, marksz = zip(*mapped)
print("The unzipped result of name list is : ", namz)
print("The unzipped result of roll_no list is : ", tuple(roll_noz))
print("The unzipped result of marks list is : ", list(marksz))
