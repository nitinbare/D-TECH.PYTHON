#string senclosed in ' ' " , " "

text = " Hello World Hello Python! "
# 1. string(), lostrip(), rstrip()
print ("Original:",text)
text1 = text.strip()
print("Strip(): ",text1)

'''
print("lstrip():" , text.lstrip())
print("rstrip():",text.rstrp())
'''

#2. lower(), upper(), capitalize(), title()
print("lower():" , text1.lower())
print("upper():",text1.upper())
print("capitalize():", text.strip().capitalize())
print("title():" , text1.title())

# 3.replace()
print("find('world'):",text.find("world"))
print("index('world'):" , text.find("java"))

#cout()
print("cout('Hello'):", text.count("hello"))

#split(), join()
world = text.strip().split(" ")
print("split():", " ".join(world))

#startswitch(), endswitch()
print("endswith('!'):", text1.endswith("!"))

#isalpha(), isdigit(), isalnum()
print(" ' abs'.isalpha():","abc".isalpha())
print("'123'.isdigit(): " ,"123".isdigit())
print("'abc123'.isalnum():" , "abc123".isalnum())

#sting indexing

name = "Madhav"

print(name[0::2])
print(name[0])
print(name[-1])

#fist character
print(name[0:1])
print(name[:1])

#first two chracters
print(name[0:2])
print(name[:2])

#3rd charecer to 5th charecters
print(name[2::])

#reverse
print(name[::-1])

#print string by 2 step
print(name[0:5:2])

#tupple

#creating a tupple
fruits = ("apple", "banana", "cherry","banana",)
print("Original Tuple:", fruits)

# count()
banana_cout = fruits.count("banana")
print("Cout of 'banana':" , banana_cout)

#index()
banana_index =  fruits.index("banana")
print("Index of 'banana':", banana_index)