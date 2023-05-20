#DAY 1
"""
1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
 The numbers obtained should be printed in a comma-separated sequence on a single line.

for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=", ")

#2.Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320
#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.

A.
x = int(input('enter number: '))
fact = 1
for i in range(1, x+1):
    fact = fact * i
print(fact)

B.
def facto(x):
    while x > 1:
        factt = x * x
        x = x - 1
        print(x, end=" * " )
       # print(factt, end=", ")

facto(9)

#3. With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.Suppose the following input is supplied to the program: 8
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.Consider use dict()

x = int(input('enter number: '))
d = {}
for i in range(1, x+1):
    d[i] = i * i
print(d)

#DAY 2
4.Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.tuple() method can convert list to tuple

x = input('enter a sequence: ').split(',')
print(x)
print(tuple(x))

5.Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
Hints:
Use init method to construct some parameters

class Cm():
    def coletInput(self):

        self.x = input('write something here: ')
    def prntInput(self):
        print(self.x.upper())

a = Cm()
a.coletInput()
a.prntInput()

6. Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 _ C _ D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
Hints:
If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26).
In case of input data being supplied to the question, it should be assumed to be a console input.

import math
D = input("input value for D: ").split(',') #splits at ','
D = [int(i) for i in D] #converts every value for D to int through looping
C = 50
H = 30
li = []
for i in D:
    li.append(str(round(math.sqrt(2*C*i/H))))
print(','.join(li))

7. Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*
Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
Hints:
Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

a = int(input('enter 1st value: '))
b = int(input('enter 2nd value: '))
lis = []
for i in range(a):
    tem = []
    for j in range(b):
        tem.append(i*j)
    lis.append(tem)
print(lis)

x,y = map(int,input().split(','))
lst = []

for i in range(x):
    tmp = []
    for j in range(y):
        tmp.append(i*j)
    lst.append(tmp)

print(lst)

8. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

word = input('enter words: ').split(',')
nw = []
for i in word:
    nw.append(i)
    nw.sort(key = str.lower)
print(','.join(nw))

9. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
def cap(x=str):
    return x.upper(text)

print(cap())

#DAY 3

10. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.

a = input('enter words: ').split(' ')
a.sort()
new = []
for i in a:
    if i not in new:
        new.append(i)
print(' '.join(new))

11. Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

a = input('enter digits: ').split(',')
b = []
for i in a:
    if int(i, 2) % 5 == 0:
        b.append(i)
print(','.join(b))

12. Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

for i in range(1000, 3001):
    if i % 2 == 0:
        print(i, end=', ')

#lst = [str(i) for i in range(1000,3001)]
#lst = list(filter(lambda i:all(ord(j)%2 == 0 for j in i), lst))   # using lambda to define function inside filter function
#print(",".join(lst))

13. Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

a = input('enter sentence: ')
letter, number = 0, 0
for i in a:
    if i.isdigit():
        number += 1
    elif i.isalpha():
        letter += 1
print(f'number of characters is: {letter}')
print(f'number of digits: {number}')

#DAY 4
14. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

a = input('enter sentence: ')
upper = 0
lower = 0
for i in a:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    else:
        pass
print(f'number of upper case is: {upper}')
print(f'number of lower case is: {lower}')

15. Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

a = input('enter value for a: ')
b = ''
total = 0
for i in range(4):
    b += a
    total += int(b)
print(total)

#DAY 5
16. Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,9,25,49,81
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

a = input('enter numbers: ').split(',')
b = [str(int(i)**2) for i in a if int(i) % 2 == 1]
print(', '.join(b))

17. Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

total = 0
while True:
    action = input("action to perform? Deposit(d), Withdrawal(w), Statement(s)\n").lower()
    am = input('how much?\n')
    if action == 'd':
        total += int(am)
    elif action == 'w':
        total = total - int(am)
    elif action == 's':
        break
    print(total)

#DAY 6
18. A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

import re
validity = re.compile(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@]).{6,12}$")
a = input('enter passwords: ').split(',')
for i in a:
    if validity.fullmatch(i):
        print(i)

19. You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers.
The tuples are input by console. The sort criteria is:
1: Sort based on name
2: Then sort based on age
3: Then sort by score
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.We use itemgetter to enable multiple sort keys.

from operator import itemgetter
lis = []
while True:
    rec = input('enter record: ').split(',')
    lis.append(tuple(rec))
    c = input('do u wish to add more record? ')
    if c == 'c':
        continue
    else:
        break

print(sorted(lis, key=itemgetter(0,1,2)))

#DAY 7
20. Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
Suppose the following input is supplied to the program:
7
Then, the output should be:
0
7
14
Hints:
Consider use class, function and comprehension.

class Itr():
    def div(self, a):
        self.a = a
        for i in range(0, int(a) + 1):
            if i % 7 == 0:
                yield i

b = Itr().div(int(input('enter range: ')))
for i in b:
    print(i)


21 A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.Here distance indicates to euclidean distance.Import math module to use sqrt function.

from math import sqrt
lst = []
position = [0,0]
while True:
    a = input()
    if not a:
        break
    lst.append(a)
for i in lst:
    if 'UP' in i:
        position[0] -= int(i.strip('UP '))
    if 'DOWN' in i:
        position[0] += int(i.strip('DOWN '))
    if 'LEFT' in i:
        position[1] -= int(i.strip('LEFT '))
    if 'RIGHT' in i:
        position[1] += int(i.strip('RIGHT '))
print(round(sqrt(position[1] ** 2 + position[0] ** 2)))

#DAY 8
22. Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
Hints
In case of input data being supplied to the question, it should be assumed to be a console input.


a = input("sentence: ").split()
di = {i:a.count(i) for i in a}  # sets dictionary as i-> split word & a.count(i) -> total occurrence of i in a
di = sorted(di.items()) # items() function returns both key & value of dictionary as a list and then sorted. The sort by default occurs in order of 1st -> 2nd key
for i in di:
    print(f'{i[0]} : {i[1]}')

23. Write a method which can calculate square value of number
Hints:
Using the ** operator which can be written as n**p where means n^p

def square(num):
    return num ** 2
print square(2)
print square(3)

n=int(input())
print(n**2)

24. Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books.
But Python has a built-in document function for every built-in functions.
Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
And add document for your own function
Hints:
The built-in document method is __doc__

print(abs.__doc__)
print(sorted.__doc__)
print(input.__doc__)

25. Define a class, which have a class parameter and have a same instance parameter.
Hints:
Define an instance parameter, need add it in __init__ method.You can init an object with construct parameter or set the value later

class C():
    nam = 'C'
    def __init__(self, name):
        self.name = name
na = C('jefferson')
print(f'{na.nam}, {na.name}')

#DAY 9
26. Define a function which can compute the sum of two numbers.
Hints:
Define a function with two numbers as arguments. You can compute the sum in the function and return the value.

def summ(x, y):
    return x + y
print(summ(2, 3))

27. Define a function that can convert a integer into a string and print it in console.
Hints:
Use str() to convert a number to string.

def conv():
    a = int(input('enter integer: '))
    return str(a)
print(conv())

28. Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.
Hints:
Use int() to convert a string to integer.

def conv(x, y):
    print(str(x) + str(y))
print(conv(3, 4))

29. Define a function that can accept two strings as input and concatenate them and then print it in console.
Hints:
Use + sign to concatenate the strings.

def strr(x, y):
    print(str(x) + str(y))
print(strr('555', 'hh'))

30. Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print all strings line by line.
Hints:
Use len() function to get the length of a string.

de strr(x, y):
    if len(x) > len(y):
        print(x)
    elif len(x) < len(y)
        print(y)
    else:
        print(x+"\n"+y)
print(strr('errrre', '37rbfnf'))

#DAY 10
31. Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
Hints:
Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.

def dic():
    dict1 = {i: i * i for i in range(1, 21)}
    print(dict1)
dic()

32. Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
The function should just print the keys only.
Hints:
Use dict[key]=value pattern to put entry into a dictionary.Use ** operator to get power of a number.Use range() for loops.Use keys() to iterate keys in the dictionary.
Also we can use item() to get key/value pairs.

def dic():
    dict1 = {i: i * i for i in range(1, 21)}
    for i in dict1.keys():
        print(i)
dic()

33. Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
Hints:
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.

def lis():
    a = [i**2 for i in range(1, 21)]
    print(a)
lis()

34. Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
Hints:
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list

def lis():
    a = [i**2 for i in range(1, 21)]
    for i in a[0:5]:
        print(i)
lis()

35. Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.
Hints:
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list

def lis():
    a = [i**2 for i in range(1, 21)]
    for i in a[-5:]:
        print(i)
lis()

36. Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
Then the function needs to print all values except the first 5 elements in the list.
Hints: Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use [n1:n2] to slice a list

def lis():
    a = [i**2 for i in range(1, 21)]
    for i in a[5:]:
        print(i)
lis()

37. Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).
Hints:
Use ** operator to get power of a number.Use range() for loops.Use list.append() to add values into a list.Use tuple() to get a tuple from a list.

def tup():
    a = (i**2 for i in range(1, 21))
    print(tuple(a))
tup()

#DAY 11
38. With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
Hints:
Use [n1:n2] notation to get a slice from a tuple.

a = (1,2,3,4,5,6,7,8,9,10)
b = a[:5]
c = a[5:]
print(b)
print(c)

39. Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
Hints:
Use "for" to iterate the tuple. Use tuple() to generate a tuple from a list.

a = (1,2,3,4,5,6,7,8,9,10)
b = tuple(i for i in a if i % 2 == 0)
print(b)

40. Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
Hints:
Use if statement to judge condition.

a = input()
if a == 'yes' or a == 'YES':
    print('Yes')
elif a == 'Yes':
    print('Yes')
else:
    print('No')

41. Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
Hints:
Use map() to generate a list.Use lambda to define anonymous functions.

a = [1,2,3,4,5,6,7,8,9,10]
b = map(lambda x:x**2, a)
print(list(b))

42. Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
Hints:
Use map() to generate a list.Use filter() to filter elements of a list.Use lambda to define anonymous functions.

a = [1,2,3,4,5,6,7,8,9,10]
b = map(lambda x: x**2, filter(lambda x : x % 2 == 0, a))
print(list(b))

43. Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
Hints:
Use filter() to filter elements of a list.Use lambda to define anonymous functions.

a = [i for i in range(1, 21)]
b = [filter(lambda x: x % 2 == 0, a)]
for i in b:
    print(list(i))

#DAY 12
44. Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
Hints:
Use map() to generate a list. Use lambda to define anonymous functions.

a = [i for i in range(1, 21)]
b = [map(lambda x: x**2, a)]
for i in b:
    print(list(i))

45. Define a class named American which has a static method called printNationality.
Hints:
Use @staticmethod decorator to define class static method.There are also two more methods.To know more, go to this link.

class America():
    @staticmethod
    def static():
        print('i am american')
a = America()
a.static()

46. Define a class named American and its subclass NewYorker.
Hints:
Use class Subclass(ParentClass) to define a subclass.*

class Parent():
    a = 'i am from america'
    print(a)
class Subclass():
        print('new yorker')
b = Parent()
c = Subclass()

#DAY 13
47. Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
Hints
Use def methodName(self) to define a method.

class Circle():
    def __init__(self, r, pi):
        self.r = r
        self.pi = pi
    def area(self):
        return self.pi * self.r**2
a = Circle(5, 3.142)
print(a.area(),'cm')

48. Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.
Hints
Use def methodName(self) to define a method.

class Rectangle():
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath
    def area(self):
        return self.length * self.breath
a = Rectangle(4, 5)
print(a.area(),'cm')

49. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
Hints
To override a method in super class, we can define a method with the same name in the super class.

class Shape():
    def area(self):
        pass
    def area(self):
        return  0
class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length
    def area(self):
        a = int(input('provide breath: '))
        b = int(input('provide height: '))
        print(self.length * a * b)
c = Shape()
d = Square(1)
d.area()

50. Please raise a RuntimeError exception.
Hints
UUse raise() to raise an exception.

raise RuntimeError('blaaaaa')

#DAY 14
51. Write a function to compute 5/0 and use try/except to catch the exceptions.
Hints
Use try/except to catch exceptions.

def zeroerr():
    try:
        return 5/0
    except ZeroDivisionError:
        print('cannot divide by zero')
zeroerr()


52. Define a custom exception class which takes a string message as attribute.
Hints
To define a custom exception, we need to define a class inherited from Exception.

class Ex(Exception):
    def __init__(self, message):
        self.message = message
a = Ex('something went wrong with your code')
print(a)

53. Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address.
Both user names and company names are composed of letters only.
Example: If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
john
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints
Use \w to match letters.

a = input('enter email address: ').split('@')
print(a[0])
print('@'.join(a))

#DAY 15
54. Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address.
Both user names and company names are composed of letters only.
Example: If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
google
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints
Use \w to match letters.

import re
a = input('enter email address: ')
pattern = "(\w+)@(\w+)+(.com)"
comapny = re.match(pattern, a)
print(comapny.group(2))

55. Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
Example: If the following words is given as input to the program:
2 cats and 3 dogs.
Then, the output of the program should be:
['2', '3']
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints
Use re.findall() to find all substring using regex.

a = input('enter sentence: ').split(' ')
b = []
for i in a:
    if i.isdigit():
        b.append(i)
print(b)

56. Print a unicode string "hello world".
Hints
Use u'strings' format to define unicode string.

print(u"hello world")

57. Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
Hints
Use unicode()/encode() function to convert.

a = input('hewllo world!')
b = a.encode('utf-8')
print(b)

58. Write a special comment to indicate a Python source code file is in unicode.
Hints
Use unicode() function to convert.

# *- coding: utf-8 -*-

59. Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
Example: If the following n is given as input to the program:
5
Then, the output of the program should be:
3.55
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints
Use float() to convert an integer to a float.Even if not converted it wont cause a problem because python by default understands the data type of a value

a = int(input('enter number: '))
n = 0
for i in range(1, a+1):
    n += i / (i+1)
print(round(n, 2))

#DAY 16
60. Write a program to compute:
f(n)=f(n-1)+100 when n>0
and f(0)=0
with a given n input by console (n>0).
Example: If the following n is given as input to the program:
5
Then, the output of the program should be:
500
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints
We can define recursive function in Python.

def fun(x):
    if x == 0:
        return 0
    else:
        return fun(x - 1) + 100
n = int(input('enter number: '))
print(fun(n))

61. The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.
Example: If the following n is given as input to the program:
7
Then, the output of the program should be:
13
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints
We can define recursive function in Python.

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
a = int(input('enter number: '))
print(fib(a))

62. The Fibonacci Sequence is computed based on the following formula:
f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1
Please write a program to compute the value of f(n) with a given n input by console.
Example: If the following n is given as input to the program:
7
Then, the output of the program should be:
0,1,1,2,3,5,8,13
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints
We can define recursive function in Python. Use list comprehension to generate a list from an existing list. Use string.join() to join a list of strings.

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
a = int(input('enter number: '))
b = [fib(i) for i in range(0, a+1)]
print(b, end=', ')

63. Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
Example: If the following n is given as input to the program:
10
Then, the output of the program should be:
0,2,4,6,8,10
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints
Use yield to produce the next value in generator.

def gen(x):
    for i in range(1, x+1):
        if i % 2 == 0:
            yield i
a = int(input('enter number: '))
print(list(gen(a)))

64. Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
Example: If the following n is given as input to the program:
100
Then, the output of the program should be:
0,35,70
In case of input data being supplied to the question, it should be assumed to be a console input.
Hints
Use yield to produce the next value in generator.

def div(n):
    for i in range(0, n+1):
        if i % 5 == 0 and i % 7 == 0:
            yield i

a = int(input('enter number: '))
b = []
for i in div(a):
    b.append(str(i))
print(', '.join(b))

#DAY 17
65. Please write assert statements to verify that every number in the list [2,4,6,8] is even.
Hints
Use "assert expression" to make assertion.

a = [2,4,6,8]
for i in a:
    assert i % 2 == 0

66. Please write a program which accepts basic mathematic expression from console and print the evaluation result.
Example: If the following n is given as input to the program:
35 + 3
Then, the output of the program should be:
38
Hints
Use eval() to evaluate an expression.

a = input('enter expression: ')
print(eval(a))

67. Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
Hints
Use if/elif to deal with conditions.
"""""
def binary_search_Ascending(array, target):
    lower = 0
    upper = len(array)
    print('Array Length:',upper)
    while lower < upper:
        x = (lower + upper) // 2
        print('Middle Value:',x)
        value = array[x]
        if target == value:
            return x
        elif target > value:
            lower = x
        elif target < value:
            upper = x

Array = [1,5,8,10,12,13,55,66,73,78,82,85,88,99]
print('The Value Found at Index:',binary_search_Ascending(Array, 82))
Array.
"""
68. Please generate a random float where the value is between 10 and 100 using Python module.
Hints
Use random.random() to generate a random float in [0,1].

69. Please generate a random float where the value is between 5 and 95 using Python module.
Hints
Use random.random() to generate a random float in [0,1].

#DAY 18
70. Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.
Hints
Use random.choice() to a random element from a list.

71. Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension.
Hints
Use random.choice() to a random element from a list.

72. Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
Hints
Use random.sample() to generate a list of random values.

73. Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
Hints
Use random.sample() to generate a list of random values.

74. Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.
Hints
Use random.sample() to generate a list of random values.

#DAY 19
75. Please write a program to randomly print a integer number between 7 and 15 inclusive.
Hints
Use random.randrange() to a random integer in a given range.

76. Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".
Hints
Use zlib.compress() and zlib.decompress() to compress and decompress a string.

77. Please write a program to print the running time of execution of "1+1" for 100 times.
Hints
Use timeit() function to measure the running time.

78. Please write a program to shuffle and print the list [3,6,7,8].
Hints
Use shuffle() function to shuffle a list.

79. Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
Hints
Use list[index] notation to get a element from a list.

#DAY 20
80. Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].
Hints
Use list comprehension to delete a bunch of element from a list.

81. By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
Hints
Use list comprehension to delete a bunch of element from a list.

82. By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
Hints
Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.

83. By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].
Hints
Use list comprehension to delete a bunch of element from a list. Use enumerate() to get (index, value) tuple.

84. By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
Hints
Use list comprehension to make an array.

85. By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
Hints
Use list comprehension to delete a bunch of element from a list.Use enumerate() to get (index, value) tuple.

86. By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
Hints
Use list's remove method to delete a value.

87. With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.
Hints
Use set() and "&=" to do set intersection operation.

88. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
Hints
Use set() to store a number of values without duplicate.

89. Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.
Hints
Use Subclass(Parentclass) to define a child class.

90. Please write a program which count and print the numbers of each character in a string input by console.
Example: If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2
c,2
b,2
e,1
d,1
g,1
f,1
Hints
Use dict to store key/value pairs. Use dict.get() method to lookup a key with default value.

91. Please write a program which accepts a string from console and print it in reverse order.
Example: If the following string is given as input to the program:*
rise to vote sir
Then, the output of the program should be:
ris etov ot esir
Hints
Use list[::-1] to iterate a list in a reverse order.

92. Please write a program which accepts a string from console and print the characters that have even indexes.
Example: If the following string is given as input to the program:
H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:
Helloworld
Hints
Use list[::2] to iterate a list by step 2.

93. Please write a program which prints all permutations of [1,2,3]
Hints
Use itertools.permutations() to get permutations of list.

94. Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
Hints
Use for loop to iterate all possible solutions.

95. Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given scores. Store them in a list and find the score of the runner-up.
If the following string is given as input to the program:
5
2 3 6 6 5
Then, the output of the program should be:
5
Hints
Make the scores unique and then find 2nd best number

96. You are given a string S and width W. Your task is to wrap the string into a paragraph of width.
If the following string is given as input to the program:
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Then, the output of the program should be:
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
Hints
Use wrap function of textwrap module

97. You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:
#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
#size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
Hints
First print the half of the Rangoli in the given way and save each line in a list. Then print the list in reverse order to get the rest.
98. You are given a date. Your task is to find what the day is on that date.
Input
A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.
08 05 2015
Output
Output the correct day in capital letters.
WEDNESDAY
Hints
Use weekday function of calender module

99. Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
Input
The first line of input contains an integer, M.The second line contains M space-separated integers.The third line contains an integer, N.The fourth line contains N space-separated integers.
4
2 4 5 9
4
2 4 11 12
Output
Output the symmetric difference integers in ascending order, one per line.
5
9
11
12
Hints
Use '^' to make symmetric difference operation.

100. You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. 
See the sample input/output for clarification.
If the following string is given as input to the program:
4
bcdef
abcdefg
bcde
bcdef
Then, the output of the program should be:
3
2 1 1
Hints
Make a list to get the input order and a dictionary to count the word frequency

101. write a program that prints the number from 1-100, but for the multiples of 3 prints 'fizz' and for the multiples of 5 prints 'buzz'. 
and for numbers that are multiples of both 3 and 5 prints 'fizzbuzz'.

a = [i for i in range(1, 101)]
b = []

for i in a:
    if i not in b:
        if i % 3 == 0 and i % 5 == 0:
            i = 'fizzbuzz'
        elif i % 3 == 0 and i % 5 != 0:
            i = 'fizz'
        elif i % 5 == 0 and i % 3 != 0:
            i = 'buzz'
        b.append(i)
print(b)

102. write a program that tells if a year is a leap year or not.

def leap_yr(year):
    if year % 4 == 0 and year % 400 == 0:
        print(f'the year {year} is leap year')
    elif year % 100 == 0:
        print(f'the year {year} is not a leap year')
    else:
        return f'year {year} is not leap'

a = leap_yr(int(input('enter year: ')))
print(a) 

"""

