'''
Multi-line comments go between 3 quotation marks.
You can use single or double quotes.
'''

# One-line comments are preceded by the  pound symbol

# BASIC DATA TYPES

x = 5  # creates an object
print(type(x))  # check the type: int (not declared explicitly)
type(x)

# LISTS

nums = [5, 5.0, 'five']  # multiple data types
print(nums)
print(type(nums))
print(len(nums))
print(nums[0])
nums[0] = 6
print(nums[0])

nums.append(7)
print(nums)
nums.remove('five')

print(sorted(nums))
print(nums)
print(sorted(nums, reverse=True))

# list slicing [start:end:step]
weekdays = ['mon', 'tues', 'wed', 'thurs', 'fri']
print(weekdays[0])  # element 0
print(weekdays[0:3])  # element 0-2
print(weekdays[:3])  # element 0-2
print(weekdays[3:])  # element 3, 4
print(weekdays[-1])  # last element
print(weekdays[::2])  # every second element
print(weekdays[::-1])  # backwards

days = weekdays + ['sat', 'sun']
print(days)

# FUNCTIONS


def give_me_five():
    return 5


print(give_me_five())


def calc(x, y, op='add'):
    if op == 'add':
        return x+y
    elif op == 'subtract':
        return x-y
    else:
        print('Valid operations: add, substract')


print(calc(5, 3, 'add'))
print(calc(5, 3, 'subtract'))
print(calc(5, 3, 'multiply'))
print(calc(5, 3))

# Write a function that takes two parameters (hours and rate), and
# return the total pay.


def compute_pay(hours, rate):
    return hours * rate


print(compute_pay(40, 10.50))


def compute_more_pay(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        return 40 * rate + (hours-40) * (rate*1.5)


print(compute_more_pay(30, 10))
print(compute_more_pay(45, 10))


def both_ends(s):
    if len(s) < 2:
        return ''
    else:
        return s[:2] + s[-2:]


print(both_ends('spring'))
print(both_ends('cat'))
print(both_ends('a'))

# FOR LOOPS
# range returns a list of integers
print(range(0, 3))

for i in range(5):
    print(i)

# print each element in uppercase
fruits = ['apple', 'banana', 'cherry']
for i in range(len(fruits)):
    print(fruits[i].upper())


# better for loop
for fruit in fruits:
    print(fruit.upper())

# EXERCISE: Write a program that prints the numbers form 1 to 100. But for
# multiples of 3 print 'fizz' instead of the number, and for the multiples of 5
# print 'buzz'. For numbers which are multiples of both 3 and 5 print 'fizzbuzz'.


def fizz_buzz():
    nums = range(1, 100)
    for num in nums:
        if num % 15 == 0:
            print(num, 'fizzbuzz')
        elif num % 3 == 0:
            print(num, 'fizz')
        elif num % 5 == 0:
            print(num, 'buzz')


print(fizz_buzz())


def front_x(words):
    lista = []
    listb = []
    for word in words:
        if word[0] == 'x':
            lista.append(word)
        else:
            listb.append(word)
    return sorted(lista) + sorted(listb)


print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))
