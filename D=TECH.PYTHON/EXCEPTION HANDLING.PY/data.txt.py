'''file = open("data.txt", "r")
content = file.read()
print(content)
file.close()


file = open("data.txt" , "r")
'''
'''file = open("C:/Users/HP/Documents/New folder/D=TECH.PYTHON/EXCEPTION HANDLING.PY/data.txt", "r")
content = file.read()
print(content)
file.close()'''
'''
file = open("C:/Users/HP/Documents/New folder/D=TECH.PYTHON/EXCEPTION HANDLING.PY/data.txt", "r")
content = file.readline()
print(content)
file.close()'''
'''
file = open("C:/Users/HP/Documents/New folder/D=TECH.PYTHON/EXCEPTION HANDLING.PY/data.txt", "r")
content = file.readlines()
print(content)
file.close()'''


'''file = open("C:/Users/HP/Documents/New folder/D=TECH.PYTHON/EXCEPTION HANDLING.PY/data.txt" , "w")
file.write("hello , world")
file.close()

file = open("C:/Users/HP/Documents/New folder/D=TECH.PYTHON/EXCEPTION HANDLING.PY/data.txt","r")
content = file.read()
print(content)
file.close()
'''

file = open("C:/Users/HP/Documents/New folder/D=TECH.PYTHON/EXCEPTION HANDLING.PY/data.txt" , "w")
file.close()

import os
os.remove('C:/Users/HP/Documents/New folder/D=TECH.PYTHON/EXCEPTION HANDLING.PY/data.txt')
