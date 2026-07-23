'''
           Regular Experession(RegEx)
           --------------------------
-RegEx is an sequece of char that can searching 

syntax-->import re


Fuctions
---------
1.findall()
---------
->it will find all the char that are in the string...
eg
--
import re
txt = 'python is a language and also called dyanamically typed'
print(re.findall('[an]',txt))
2.search
-----------
import re
txt = 'python is a language and also called dyanamically typed'
print(re.search(' ',txt))
   
3.split
--------
eg-
import re
txt = 'python is a language and also called dyanamically typed'
print(re.split(' ',txt))

4.sub
-------
eg-
import re
txt = 'python is a language and also called dyanamically typed'
print(re.sub(' ','&',txt))

5.fullmatch
-----------
metachar
----------
1.[]- we can give range character and number for relaible fuctions.
ex-
import re
txt = 'I have 100 Rupees'
print(re.findall('[0-9]',txt))
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))

print(re.search('[0-9]',txt))
print(re.search('[a-z]',txt))
print(re.search('[A-Z]',txt))

2.^ -checks the end end characeter in string it meeting condition are not.
ex-
import re
txt = 'I have 100 Rupees'
print(re.findall('^I have',txt))
print(re.search('^I have',txt))

3.$- checks the end character in string it meeting its condition are not.
ex-
import re
some = 'I am going to school'
print(re.findall('school$',some))
print(re.search('school$',some))
4. '.'- return the string haivng no. of dots the condition meets
ex-
import re
some = 'I am going to school'
print(re.findall('A...',some))
print(re.search('A...',some))
5.*
eg-
import re
how = 'python is language'
print(re.findall('p.*n',how))
print(re.findall('p.*ython',how))
print(re.findall('p.*n',how))
6.+
eg-
import re
how = 'python is language'
print(re.findall('p.+a',how))
print(re.search('p.+p',how))
7.{}
eg-
import re
how = 'python is language'
print(re.findall('{10}',how))
print(re.search('{10}',how))

















'''





























