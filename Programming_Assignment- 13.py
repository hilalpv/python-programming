#Question 1: Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
D = [int(x) for x in input("Enter two values\n").split(',')]
C = 50
H = 30
import math
def func_q(D):
    for i in D:
     X = (2 * C * i)/H
     Q = math.sqrt(X)
    return Q

print(func_q(D))

#Question 2 Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡¬Y-1.

def func_a(X,Y):
 arr = [[i for i in range(X)] for j in range(Y)]
 return arr

print(func_a(3,4))

# Question 3:
# Write a program that accepts a comma separated sequence of words as input and
# prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be: bag,hello,without,world
a, b = map(int, input("Enter two values\n").split(', '))
print("\nThe value of a is {} and b is {}".format(a, b))


# Question 4:
# Write a program that accepts a sequence of whitespace separated words as input and
# prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
list_x = input("Enter two values\n").split(' ')
list_x.sort()
print(set(list_x))

# Question 5:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3
string_1 = input(str("enter a string"))
letters = 0  # initiating the count of letters to 0
numeric = 0  # initiating the count of numbers to 0

for i in string_1:
    if i.isdigit():
        numeric +=1
    elif i.isalpha():
        letters +=1
    else:
        pass
print(letters)
print(numeric)

# Question 6: A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma.
Password = input("Enter a password")
import re
x = True
while x:
    if (len(Password)<6 or len(Password)>12):
        break
    elif not re.search("[a-z]",Password):
        break
    elif not re.search("[0-9]",Password):
        break
    elif not re.search("[A-Z]",Password):
        break
    elif not re.search("[$#@]",Password):
        break
    elif re.search("\s",Password):
        break
    else:
        print("Valid Password")
        x=False
        break
if x:
    print("Not a Valid Password")
