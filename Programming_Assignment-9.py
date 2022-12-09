# 1.	Write a Python program to check if the given number is a Disarium Number?
dis_num = 175

valid = 0
for i, j in enumerate(str(dis_num)):
    print(i + 1, j)
    valid = int(j) ** (i + 1) + valid
print(valid)

if dis_num == valid:
    print(dis_num, ' is a Disarium number')


# 2.	Write a Python program to print all disarium numbers between 1 to 100?
def calculate_length(n):
    length = 0
    while (n != 0):
        length = length + 1
        n = n // 10
    return length


def sum_of_digit(num):
    rem = sum = 0
    len = calculate_length(num)

    while (num > 0):
        rem = num % 10
        sum = sum + (rem ** len)
        num = num // 10
        len = len - 1
    return sum


result = 0

print("disarium numbers between 1 and 100 are")
for i in range(1, 101):
    result = sum_of_digit(i)

    if (result == i):
        print(i)

# 3.	Write a Python program to check if the given number is Happy Number?

num = 121


def isHappyNumber(num):
    sum = rem = 0
    while num > 0:
        rem = num % 10
        sum = sum + (rem * rem)
        num = num // 10
    return sum


result = num
while (result != 1 and result != 4):
    result = isHappyNumber(result)

if (result == 1):
    print(str(num) + " is a happy number")
elif (result == 4):
    print(str(num) + " is not a happy number")


# 4.	Write a Python program to print all happy numbers between 1 and 100?

def isHappyNumber(num):
    rem = sum = 0
    while num > 0:
        rem = num % 10
        sum = sum + rem * rem
        num = num // 10
    return sum

    i = 0


for i in range(1, 101):
    result = i
    while result != 1 and result != 4:
        result = isHappyNumber(result)
        if (result == 1):
            print(i)
            print(" ")

# 5.	Write a Python program to determine whether the given number is a Harshad Number?
num = 180
def cal_sum(num):
    s_sum = 0
    temp = num
    while temp > 0:
        s_sum = s_sum + temp % 10
        temp = temp // 10
    return s_sum


def Is_Harshad_Number(num):
    if num % cal_sum(num) == 0:
        print(num, " is Harshad Number")
    else:
        print(num, " is not a Harshad Number")

Is_Harshad_Number(num)

# 6.	Write a Python program to print all pronic numbers between 1 and 100?
num = 110
n = 0

def is_pronic_num(num):
    sqr_rt = num**(1/2)
    floor = sqr_rt // 1
    celling = floor+1
    return floor * celling

if is_pronic_num(num) == num:
    print(num, "this is pronic number")
else:
    print(num, "this is not pronic number")