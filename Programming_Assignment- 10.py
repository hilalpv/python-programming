#  1.Write a Python program to find sum of elements in list?

def sum_list(a_list):
    for i in a_list:
       s_sum = sum(a_list)
    return s_sum

a_list = [2,6,7]
print(sum_list(a_list))

#  2.Write a Python program to  Multiply all numbers in the list?

def mul_list(a_list):
    mul = 1
    for i in a_list:
        mul = mul * i
    return mul

a_list = [2, 6 ,8]
print(mul_list(a_list))

#  3.Write a Python program to find smallest number in a list?

def min_x(a_list):
    min_list = 100000
    for i in a_list:
            if min_list >  i:
                min_list = i
    return min_list

print(min_x(a_list))

# 4.	Write a Python program to find largest number in a list?
print(max(a_list))

# 5.	Write a Python program to find second largest number in a list?
sorting = a_list.sort()
print("Second largest element is:", a_list[-2])

# 6.	Write a Python program to find N largest elements from a list?

n = 3
sorting = a_list.sort()
print("N largest element is:", a_list[-n:])

# 7.	Write a Python program to print even numbers in a list?
def even_num(a_list):
    new_list =[]
    for i in a_list:
        if  i % 2==0:
            new_list.append(i)
    return new_list
print("even number list is:", even_num(a_list))

## 8.	Write a Python program to print odd numbers in a List?
def odd_num(a_list):
    new_list =[]
    for i in a_list:
        if  i % 2!=0:
            new_list.append(i)
    return new_list
print("odd number list is:", odd_num(a_list))

## 9.	Write a Python program to Remove empty List from List?
a_list= [1,2,3,[],[],56]
new_list =[]
for i in a_list:
    if i != []:
        new_list.append(i)
print(new_list)

## 10.	Write a Python program to Cloning or Copying a list?
a_list= [1,2,3,[],[],56]
new_list =[]
for i in a_list:
    new_list.append(i)
print(new_list)

## 11.	Write a Python program to Count occurrences of an element in a list?
def count_x(a_list):
    x=56
    count_v = a_list.count(x)
    return count_v
print(count_x(a_list))


