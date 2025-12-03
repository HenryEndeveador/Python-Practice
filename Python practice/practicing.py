# List operations

list = ['Jme', 'gjd', 'fgd', 'lll']

copy_list = list.copy() #If you don't use copy(), any changes you make to copied list will also be made on the original.

copy_list.append('564')

print(list)
print(copy_list)


second_list = [['bro'], ['bro 2']]

second_list[0].append('bro 1')
second_list[1].extend('bro 3')
print(second_list)

# tuples 

empty_tuple = (45, 67, "Bob", "Dat")

print(type(empty_tuple))

 # A tuple item cannot be modified.

 #so the following is not allowed

# empty_tuple[0] = 46 # this will give an error

# dictionaries

#two ways of creating a dictionary 

my_dict = {}

my_dict = dict()

student = {"name": "Toyosi", "age": 17, "major": "Electrical Engineering"}

print(student)
print(student.get("name")) #it's better to use .get for error handling. If name wasn't found, this wont throw an error
print(student['name']) #this will however 

student.update({"age": 25})
print(student["age"])

# keys should always be unique in a dictionary