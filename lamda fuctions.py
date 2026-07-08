'''
-------------------lambda fuction-----------------

->this is also called as annonymous fuction..
->A lambda fuction can take n number of agruments but having only one expression
syntax-> lamda agruments : experssion

some = lambda an,so,why : an + so + why
print(some(10,8,2))

filter()
-------------------
->The filter() fuction is a built-in used to filter elements from an itterables such is list, tuple and set based on condition
syntax-->filter (fuction return  object so we can convert that into list, set tuple
num = [1,2,3,4,5]
rev = filter(lambda a: a%2 !=0,num)
print(set(rev))

num = [1,2,3,4,5]
rev = filter(lambda a: a%2 !=0,num)
print(tuple(rev))

num = [1,2,3,4,5]
rev = filter(lambda a: a%2 !=0,num)
print(set(rev))

--------------list comprehension-------------
->This offers a shoreter syntax when we want to create a new list from the old
syntax-> varible_name = [expression loop condition]

old_ = [1,2,3,4,5,6]
new_ = [j for j in old_]
print(new_)

old_ = [1,2,3,4,5,6]
new_ = [j for j in old_ if j % 2 == 0]
print(new_)

Dictionary comprehesion
-------------------------
->This offers a shorter syntax when we want to create a new dict from the old dict
syntax-> vaible_name = [expression loop]

old_dict = {1:2,3:4,5:6}
new_dict = {i:j for (i,j) in old_dict.items() if j % 2 == 0}
print(new_dict)









'''
old_dict = {1:2,3:4,5:6}
new_dict = {i:j for (i,j) in old_dict.items() if j % 2 == 0}
print(new_dict)





