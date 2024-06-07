#lists - it is an inbuilt function in python that can store multiple values
      #- it is mutable

#create list
my_list=[1,2,3,4,5]

#adding an element
my_list.append(6)
#removing an element
my_list.remove(3)

#modify the list
my_list[0]=10

print("updated list",my_list)

#dictionary-
# creating a dictionary
my_dict={'name':'john','age':25,'city':'Delhi'}

#adding
my_dict['gender']='Male'
print(my_dict)

#removing 
del my_dict['age']
print(my_dict)

# modifying
my_dict['city']='Mumbai'
print("updated dictionary is",my_dict)

#creating a set
my_set={1,2,3,4,5}

#adding
my_set.add(6)

#removing
my_set.remove(3)

#modifying 
my_set.discard(1)
my_set.add(10)
print(my_set)
