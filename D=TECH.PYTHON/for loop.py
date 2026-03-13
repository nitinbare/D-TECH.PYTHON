'''for i in range(20):
    print(i)'''
'''for i in range(10 , 16):
        print(i)'''


'''for i in range(2,21,2):
     print(i) '''      


'''L = ["Apple", "Banana", "Chery"]
for fruit in L :
    print(fruit)'''

'''s = "abc"
for x in s :
    print(x)'''

# List

'''num = [1,2,3,4,5]
for n in num:
    print(n)'''

#stop when numis 3

'''num =[1,2,3,4,5]
for n in num:
    if n == 3:
        break
    print(n)'''

#  skip number 4
'''num =[1,2,3,4,5]
for n in num:
    if n == 4:
        continue
    print(n)'''

# pass keyword:

'''num =[1,2,3,4,5]
for n in num:
    if n == 4:
       pass
    print(n)'''

'''a = [10,20,30,40,50]
for num in a:

    print (num * 2)'''

# star paturn

'''for i in range(1,6):
    print("*" * i)''' 

#while loop
'''
i = 1
while i <= 5:
    print(i)
    i+=1
    '''
#
'''while True:
    print("Hello")
    '''
# break 
'''
i = 1
while i <= 10:
    if i == 6:
        break
    print(i)
    i+=1'''

# continue 
'''
i = 1
while i <= 10:
    if i == 6:
        i += 1
        continue
    print(i)
    i += 1
    '''

# Even number
'''
i = 1
while i<= 20:
    if i%2 ==0:
        print(i)
    i+=1
    '''

# sum of first 10 num:
'''
i = 1
total = 0
while i <=10:
    total += i
    i+=1
print("sum:",total)
'''

# reversed method
'''num = 1234
reversed = 0
while num >0:
    digit = num%10
    reversed= reversed*10/ digit
    num = num //10
    print("reversed:", reversed)
'''

# palindrome
num = int(input("Enter a num:"))
original = num
reversed = 0
while num>0:
    d = num % 10
    reversed = reversed *10 +d
    num = num // 10

if original == reversed:
    print(f"{num} if palindrome")
else:
    print(f"{num} is not palindrome")
