''''
# Binary file - data is in binary format (0 and 1)
#  usefull for reading and writing nib text file
#  ex - image , videos , custom binary files
# 
# use built in open() function with "b" mode
# 
# rd - read binary
# wd - read binary
# ad - append binary
# rd+ - read and write binary
# 
# text file - read and write
# r+ - read and write text file
# '''

# writing binary file

'''with open("Example1.bin","wb") as file:
    data= b"Hello everyone! this is binaary file"
    file.write(data)
    
# reading binary files

with open("Example1.bin" ,"rb") as file:
    content= file.read()
    print(content)'''
    
# copy image fie into another

with open("neature.jpg", "rb") as src:
    with open ("Copy_neature_img.jpg","wb") as dest:
        dest.write(src.read())