''' 
Given number is prime or not
--------------------------------

num = int(input('Enter a number'))
count = 0
for j in range(1,num+1) :
    if num % j == 0 :
        count += 1
        print(count)
if count == 2:
   print(f"{num} is a prime")
else:
     print(f"{num} is a not prime")


Genarating prime number in given range
----------------------------------------

limit_ = int(input('enter a value: '))
for j in range(2,limit_+1):
    count = 0
    for i in range(1,j+1):
        if j % i ==0:
            count += 1
            print(count)
    if count == 2:
        print(f"{j} is a prime")

    '''
num = 5
for j in range(1,num+1):
    for i in range(1,j+1):
     print("*",end = " ")
    print()

num = 5
for j in range(1,num+1):
    for i in range(1,j+1):
     print(j,end = " ")
    print()

num = 5
for j in range(1,num+1):
    for i in range(1,j+1):
     print(i,end = " ")
    print()

num = 4
count = 0
for j in range(num,0,-1):
    for i in range(1,j+1):
        count += 1
    print(count, end = " ")
print()

#Given number is armstrng

am_str = int(input("enter a number: "))
length_ = len(str(am_str))
all_sum = 0
for j in str(am_str):
    all_sum += int(j) ** length_
if all_sum == am_str:
    print(f"{am_str} is armstrong")
else:
    print(f"{am_str} is not a armstrong")
#primid
num = 100
for j in range(num):
    print(" "*(num-j-1),end = " ")
    print("*"*( 2* j + 1))



                

