# create an empty list
my_list = []

# append these elements
my_list.append(10),
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

# insert 15 at the second position
my_list.insert(1,15)
print(my_list)

# extend with another list
another_list = [50, 60, 70]
my_list.extend(another_list)
print(my_list)

# remove the last element on the list
del my_list[-1]
print(my_list)

# sort my list in ascending order
my_list.sort()
print(my_list)

# print index of the value 30
index_of_30 = my_list.index(30)
print(index_of_30)

