** Basics of Python                                                                                                                                                                                         02/11/2026
-Python is a high-level, dynamically typed multiparadigm programming language.
-Python code is often said to be almost like pseudocode, since it allows you to express very powerful ideas in very few lines of code while being very readable. 
_________________________________________________________________________________________________________________________________________________________________________________________________________________________
**-KEYWORDS: a keyword is a reserved or predefined word whose meaning is known to python.
-al python keywords are lower case letters, python contains 35 keywords
ex: and, as, break, class, continue, def, del , elif, else, except , exec, finally , for, from, global, if , import, in , is, lambda, not, or, pass, print, raise, returm, try, whie, with, yield.
_________________________________________________________________________________________________________________________________________________________________________________________________________________________
**Python Identifiers: identifier is a name  used to identify a variable , function, class, module or any other objects.
rules: can contain A-Z, a-z, 0-9, _(underscore)
-cannot be a keyword
-cannot start with (0-9)
ex: empName, item_name, itemPrice123
_________________________________________________________________________________________________________________________________________________________________________________________________________________________
print : print('hello Joeyyy!')
o/p: hello Joeyyy!
>> n1=20
>>n2=10
>>sum=n1+n2
>>print (sum)    o/p: 30
_______________________________________________________________________________________________________________________________________________________________________________________________________________________
 ** Fundamental types: 
1. Numeric (int, float, complex)
2. Boolean
3. String
4.Sequence(list, tuple)
5. Set
6. Dictionary

1.A)--Integer: real number without a decimal point.
--Default value of an integer is zero = false
non default value other than zero = True
a = 9
b = 3
print(a+b)  --o/p: 12

B). Float: real number with deciaml point .
-- default value:0.0, non default : all other values
ex: 3.2
>>bool (a) #true
>>type(a) # <class 'float'>
>> id(a) # 0*12 (random address..)

c). complex: Complex literals can be created by using the notation x + yj where x is the real component and y is the imaginary component.
ex: j = 1.0 - 2.0j
j
>>type(j)
>>print(j.real, j.imag) ---o/p : 1.0 -2.0

2.Boolean: Boolean can be defined by typing True/False without quotes
Ex: b1 = True
b2 = False
type(b2) --o/p: bool
____
ex: a=10
>>bool(a)  --o/p true

3.String: String is collection of charecters. in python strings are represented using 'single', "double" and '''triple''' quotes  , triple quotes are used for string multiple lines.
ex: name1 = '''my "name" is joey's tribiani'''
name2 = "my \"name\" is joye's tribiani"
name3 = """ "my" name i's joye """
____________________________________________________________________________________________________________________________________________________________________________________________________________________
**VARIABLES: A variable is a name used to store a value in memory.
A variable in Python is defined through assignment. There is no concept of declaring a variable outside of that assignment.
--In Python, you don’t need to declare the type.
rules: can contain A-Z, a-z, 0-9, _(underscore)
-cannot be a keyword
-cannot start with (0-9)
Ex: x = 10
name = "Harshitha"
price = 99.5
Single assignment: x = 5
Multiple assignment: a, b, c = 1, 2, 3
Assign same value to multiple variables: x = y = z = 100
____________________________________________________________________________________________________________________________________________________________________________________________________________________
**Dynamic Typing:In Python, while the value that a variable points to has a type, the variable itself has no strict type in its definition. 
You can re-use the same variable to point to an object of a different type. It may be helpful to think of variables as "labels" associated with objects.
x = 10        # int
x = "Hello"   # now string

--Checking Variable Type
x = 10
print(type(x))
____________________________________________________________________________________________________________________________________________________________________________________________________________________
** Type casting : 
1. implicit type casting: python automatically converts one data type to another data type during an operation
2. explicit type casting: with this conversion there is risk of data loss, since we are forcing an expression to be in some specific data type.
a). INT---> float, complex, bool, str
b). Float: bool, int, complex, str
c). complex-->bool, str
d).bool--> int, float, complex, str
e)str---> int, float, complex, bool, list, tuple, set
f)list---> bool, str, tuple, set, dict
g)tuple---> bool, set, str, list, dict
h)set----> bool, str, list, tuple, dict
i) dict---> bool, string, tuple, set
_______________________________________________________________________________________________________________________________________________________________________________________________________________________
*** operators in python: keyword which  is  used to perform specific operation on operands(variables or values)

1. Arithmetic Operators
a = 10
b = 4
print(a + b)   #14                                                                                                                
print(a - b)    #6                               
print(a * b)   #40
print(a / b) (true division) #2.5
print(a % b)  (modulus) -- returns remainder of 2 numbers   #2
print(a ** b) (power)--only performs power operation on single value datatype(int, float, bool, complex)  #10*10*10*10 =  1000
print(a // b) #floor division-- divide the two operands and returns the integer part of the result. # 2

----------------------------------------------------------------------------------------------------------------------------------------------
2. comparison operations or relational operators

a = 5
b = 7
print(a == b)  False
print(a != b)  #True
print(a < b)   #True
print(a > b)   #False
print(a <= b)  #True
print(a >= b)  #False
--------------------------------------------------------------------------------------------------------------------------------------------------
3. logical operations 

x = True
y = False
print(x and y)  #False
print(x or y)   #true
print(not y)     #true
------------------------------------------------------------------------------------------------------------------------------------------------
4.#assignment operations

x = 5
x = +5
x = -5

x += 5   #--> x = x+5
x -= 5   #--> x = x-5
x *= 3   #---> x = x*3
print(x)   #-15

________________________________________________________________________________________________________________________________________________________________________________________________________________________
name= str(input("enter your name:" ))
print("hello" , name)
print(type(name))
#Hello 1
<class 'int'>
----------------------------------------------------------------------
#f string 
age = 48
type(age)
year = 1978
x = f"I am {age} years old, born in {year}"
# # type(x)
print(x)
-------------------------------------
language = "python"
subject = 'xyhy'
print("I love {}, my subject is {}".format(language,subject))
# I love python, my subject is xyhy
---------------------------------------------------

## Simple Expressions

### Boolean Evaluation: Boolean expressions are created with the keywords and, or, not and is. For example:
and → True if both conditions are True
or → True if at least one condition is True
not → Reverses the result (True → False, False → True)
is → True if two objects are the same object in memory(True is True: true, True is False: false)
_______________________________________________________________________________________________________________________________________________________________________________________________________________________

## Branching/ conditional statement (if / elif / else): these are the control statements that execute a block of code based on the condition.

Python provides the if statement to allow branching based on conditions.
  Multiple elif checks can also be performed followed by an optional else clause.
  The if statement can be used with any evaluation of truthiness.

  1.if condition:  executes if condition is True
Ex:  age = 18
if age >= 18:
    print("You are eligible to vote.")

  2. elif another_condition: code if another_condition is True
age = 16

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

  3. else: code if none of the above conditions are True   
if - elif - else
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


