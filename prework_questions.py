# 1. Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
# The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(user_name):
    print("Hello " + user_name + "!")

hello_name("Jill")


# 2. Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

def first_odds(num):
    for num in range(100):
        if num % 2 == 0:
            print("-")
        else:
            print(num)

first_odds(0)

# 3. Please write a Python function, max_num_in_list to return the max number of a given list.
# The first line of the code has been defined as below. def max_num_in_list(a_list):

a_list = [20,40,10,100]

def max_num_in_list(a_list):
    max_number = a_list[0]

    for num in a_list:
        if num > max_number:
            max_number = num
    print(max_number)
    return max_number

max_num_in_list(a_list)


# 4. Write a function to return if the given year is a leap year.
# A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400.
# The return should be boolean Type (true/false). def is_leap_year(a_year):

def is_leap_year(a_year):
    if a_year % 4 == 0 or a_year % 400 == 0:
        return True
    else:
        return False

is_leap_year(2000)


# 5. Write a function to check to see if all numbers in the list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
# The return should be boolean Type. def is_consecutive(a_list):

a_list = [1,2,3,4,5]

def is_consecutive(a_list):
    for num in range(len(a_list) - 1):
        if a_list[num + 1] - a_list[num] != 1:
            print("not consecutive")
            return False
    print("consecutive")
    return True


is_consecutive(a_list)