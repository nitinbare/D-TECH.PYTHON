#int data type
'''
a = 10
print (a)
print(type[a])
b = -10
print  (b)
print(type[b])

#float data type
m= -10.5
print(m)
print(type[m])

n = 22.5
print(n)
print(type[n])

#complex data type
c = 2 + 3j
print(c)
print(type[c])

#Boolean data type

a = True
print(a)

b = False
print(b)
'''

#set data 
'''

my_set = {1,2,3,4}
print(my_set)
print(type[my_set])

s ={1 ,2, 2,3}
print(s)

s.add(4)
print(s)

s.remove(2)
{1 , 2  ,4}
#remove
#s.remove(20)

#discard
s.discard(20)
'''
'''
# unian intersrction
a ={1,2,3}
b ={3,4,5}
print (a|b)
print(a&b)

print(a&b |a.intersection (b))
'''

#sementric difference
'''
a = {1 , 2}
b = {4, 5}
print(a.difference(b))
print(b.difference(a))

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))


a1 = a.copy()
print(a1)
'''
'''
# sub set method
a ={1,2}
b= {1,2,3,4}

print(a.issubset(b))
print(b.issubset(a))
print(b.issuperset(a))
print(b.issuperset(a))
print(a.issuperset(b
'''
'''
#dictionary data type
d1 = {
    "name" :"Nitin",
    "age" : 23,
    "cource" :"Data"
}
print(type[d1])

#Access method
print(d1["name"])
d1.get("city","pune")
d1.get("name")
#add / update
d1["age"] = 24,
d1["city"] = "Mumbai"
d1.update({"grade" :"A"})
print(d1)

#Remove Methods
#1)pop
d1.pop("age")
# 2)popitem()

d1.popitem()
#d1.clear()
#print(d1)

#view

d1.keys()
d1.values()
d1.items()
print(d1)

#copy
d2 = d1.copy
print(d2)
'''
"""
#add element
l1 =[10 ,20, 30 , 40]
#add 50
l1.append(50)
l1.insert(1 , 15)

l1.extend([60 , 70])
#print(l1)

#remove element
l1.remove(20)
l1.pop()
#l1.clear()

#access amd search
l1[0]
l1.index(30)
l1.count(16)
print(l1)
"""
#sort and reverse

l2 = [10 ,5 ,8 ,15]
l2.sort(reverse=True)

l3 = [10, 5 ,8 ,15]
l3.sort()

l3.reverse()
print(l3)
l2.clear()
print(l2)

# type casting
'''a = 2
b = 2.5
c = a+b
print(c)'''