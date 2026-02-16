***LOOPS: In general, statements are executed sequentially. A loop in Python is used to repeat a block of code multiple times until a condition becomes false or until all items in a sequence are processed.
To avoid writing the same code again and again
To iterate over lists, strings, tuples, etc.
To perform repetitive tasks automatically
FOR LOOP: Used when you know how many times you want to repeat something or when looping through a sequence.
Syntax:
for variable in sequence:
    # body
 -- ex: For Loop with List
fruits = ["apple", "banana", "mango"]
for a in fruits:
    print(a)            #apple
                        banana
                        mango

--For Loop with String
name = "Harsh"
for a in name:
    print(a)       #H   a   r  s  h
----------------------------
# Program to find the sum of all numbers stored in a list

numbers = [1,2,3,4,5,6,7,8,9,10,11]
sum = 0
# iterate over the list
for i in numbers:
    summ+=i
    # print(i)
# Output: The sum is 48
print(sum) #66
--------------------------------------------
Program to find the sum of all numbers stored in a list
--If you are concatenating strings, start with an empty string ("") not 0.
numbers = ["joey","ruchik","kota"]
# variable to store the sum
summ=''
# iterate over the list
for i in numbers:
    # summ = i+" "+ summ
    summ = summ + " " + i
    # print(i)

# Output: The sum is 48
print(summ)            # o/p : joey ruchik kota








