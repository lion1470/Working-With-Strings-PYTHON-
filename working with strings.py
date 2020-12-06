#if we want to use text in python, we have to use strings.
#a string is created by entering text between two single or double quotation marks.
myVar = "abdullah\nkhan"
# \n = next line
my_name = "anas khan"
        #  123456789
print(myVar)
print(my_name)
print(my_name.lower())
print(my_name.upper())
print(len(my_name)) #It show that how many characters are presents in that variable
print(my_name[6])
print(my_name.index("k"))
print(my_name.replace("anas","abdullah"))
print(my_name.upper().islower())
#some charactor cant be directly included in a sring for instance, double quotes cant be directly include in a double quote string.
#charactor like these must be escaped by placing a Bsckslash before them.
#double quote only need to escaped in double quote strings, and the same is true for single quote strings.
#BACKSLSHES can also be used to escape tabs, arbitary Unicode charactor, and various other things that cant be reliby printed.
print('there was a boy name: anas he\'s not good in physics')
print("spam " * 3)#The parentheses between two
print("4" * 2)
print("abdullah " + "anas")
