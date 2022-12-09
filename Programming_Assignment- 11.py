##1. Write a Python program to find words which are greater than given length k?
names = ['kenny', 'aditi', 'lakshmi', 'deepthi', 'rahul']
new_list = []
for i in names:
    k = 5
    if len(i) > k:
        new_list.append(i)
print(new_list)

## 2. Write a Python program for removing i-th character from a string?
character = "aditigoyal"
new_char = character.replace(character[5], '')
print(new_char)

##3. Write a Python program to split and join a string?
character = "aditi_goyal"
new = character.split('_')
print(new)
new_x = ''.join(new)
print(new_x)

## 4.	Write a Python to check if a given string is binary string or not?

string = "11090985984987"

for char in string:
    flag = True
    if char == "0" or char == "1":
        continue
    else:
        flag = False
        print("This string is not a binary string")
        break
if (flag):
    print("The String is binary string")

##5  Write a Python program to find uncommon words from two Strings?
a = "aditi goyal data analyst"
b = "aditi shadowfax"


def uncommon(a, b):
    list_a = a.split()
    list_b = b.split()
    uc = ""
    for i in list_a:
        if i not in list_b:
            uc = uc + " " + i
    for j in list_b:
        if j not in list_a:
            uc = uc + " " + j

    return uc


print(uncommon(a, b))

## 6.	Write a Python to find all duplicate characters in string?

e = "aditi goyal shadowfax goyal data analyst"

def duplicate_finder(e):
    list_e = e.split(' ')
    duplst = []
    for i in list_e:
        if list_e.count(i) > 1:
            if i not in duplst:
                duplst.append(i)
    return duplst
print(duplicate_finder(e))

## 7.	Write a Python Program to check if a string contains any special character?
text = 'This is my text with special character (👽)'

from string import printable

if set(text).difference(printable):
    print('Text has special characters.')
else:
    print("Text hasn't special characters.")


