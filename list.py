'''
    list datatype:
    ->List is collection of different datatypes are enclosed in [] separeted by,
    ->List is mutable
    ex-
    all_type = [1,'python',[1,2]]

    imautable:                             mutabel:
    ->the dataype can be modified          ->any_ = [1,2,3,4]
    ex:                                     print(any_.append(1))
    so = 'python is best'                   print(any_)
    print(so.replace('python','java'))
    print(so)

    list methods:
    -----------------
    1.append():
    ex:
    any_ = [1,2,3,4,5]
    print(any_)
    any_append(5)
    print(any_)

    2.exetend:
    ->This is also add a item in the last index position, but it will give each value in each value in the each index position
    ->This will take only iterable...
    ex:
    any_ =[1,2,3,4]
    any_.extend('python')
    print(any_)
    print(len(any_))

    any_ =[1,2,'python is a language',[45,8,"java is a language",[1,23],90],'Hello']
    print(any_[3])
    print(any_[3][2][10])
    print(any_[3][3][1])

    3.pop:
    ->used to del the value from the list, but it will del based on index position
    ex-
    any_ = [1,20,30,40,50,60]
    any_.pop(5)
    print(any_)

    4.remove():
    ->used to del the item from the list, but it will del direct value from list
    syntax--> varible_name.remove(value)
    any_ = [1,2,45,8,23,90]

    tuple:
    -----------------------
    ->tuple is a collection of different represent in () and seperated by,
    ->it is immutable 
    how = (1,2,3,4,"python",[4,5],(90,78))
    print(how[4])

    tuple methods
    ----------------------
    index()
    count()
    '''





