'''a = [1,2,3]
b = [ 1,2,3]
print(a is b) #false 
print(a == b)# true

list = [1,2,2,3,2,4,1,2]
list = set (list)
l1 = set(list)
list1 = list(l1)

lst = [1,20,4,45,99]
lst.sort()
print(lst[-2])'''

'''a = [1,2,3]
b = [2,3,4]
print(list(set(a) & set (b)))'''

'''
s = 'Nitin BARE'
s1 = s.split()
print(s1)
print(len(s1))'''

#  check the string is palindrome

'''s = "python"
s1 = s[::-1]
print(s == s1)'''
# odd even
'''i = int(input("Enter the number"))
def even_odd():
    if i% 2 ==0:
        print("Number is even")
    else:
        print("number is odd")'''
        
# write a program to check positive negative  or zero
'''i = int(input("Enter the number:"))
if i >0:
    print("Number is positive")
elif i < 0:
    print("number negativenumber")
else:
    print("number number zero")'''
    
# finde the largest of threee number
'''a = 10
b = 20
c = 33
if (a> b )and(a>c):
    print("a is greater")
elif (b< a) and(b>c):
    print(f"{b}is greater");
else:
    print(f"{c}is greater")'''
'''    
marks = int(input("Enter the marks:"))
if marks >100 and marks<= 200:
    print("first class")
elis marks >  and  marks <=70
    print("Second class")'''
    
'''for i in range (10):
    print(i)'''
'''for i in range(1 ,11):
    print(i)
'''

# write a program to finde sum of given number

# write a program to finde to prime number
#soll
# write a program to print reverse of a number
l1 = [10 ,5, 8 ,15]
l1.sort(reverse= True)

l2 = [10 ,5, 8, 15]
l2.sort()

l2.reverse()
print(l2)
l1.clear()
print(l2) 