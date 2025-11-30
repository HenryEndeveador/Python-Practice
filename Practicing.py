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
