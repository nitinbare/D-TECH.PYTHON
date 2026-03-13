'''# Regular expression

def add (a,b):
    return a+b
print(add(10,3))


#  even and odd number

is_even=lambda num : True if num%2==0 else False
print(is_even(5))

def is_even():
    num=28
    if num %2==0:
        return True
    else:
        return False
'''

# find max number betwise two

max_num = lambda a,b: a if a>b else b
print(max_num(10,20))

def max_number(n1,n2):
    if n1>n2:
        print(f"{n2} is greater than {n2}")
    else:
        print(f"{n2} is greater than {n1}")
        
# Question : check number is positive or negative

number = lambda a: True if a>=0 else False
print (number(-5))

#1  map() - it used for mapping each in seq
# syntax - map (function , iterable)

list1 = [1,2,3,4,5]

# i have one list and want to calculate square of each element
# so it give me new object

square = map(lambda x: x**2, list1)
print(tuple(square))

# 2 filter() - it used to applay specific
#filter on the square the sequence
# syntax - filter(function, iterable)

list1 = [1,2,3,4,5]
even = filter(lambda x: x%2==0,list1)
print(list(even))

# reduce()- used to reduce a  seq of element into a singel value
# functool - module
# sum of numbers

from functools import reduce
number = [1,2,3,4]
result = reduce(lambda x,y :x+y,number)
print(result)

# find max number from the list

from functools import reduce
number = [1,2,3,4]
max = reduce(lambda x,y:x if x>y else y,number )
print(max)