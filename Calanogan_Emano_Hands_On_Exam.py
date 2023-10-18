print('''~~~~~~~~~~~~~~~~~~~~~~~~~
NUMBER SYSTEM CONVERSION''')

print('''~~~~~~~~~~~~~~~~~~~~~~~~~
By: Hally Emano 
    Lyle Calanogan''')
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
convert = int(input(''' Enter type of conversion 
1 = Binary Conversion
2 = Octal Conversion
3 = Hexadecimal Conversion
Enter type:'''))
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
if convert == 1:
    num = int(input("Enter a number:"))
    print(format(num, "b"))
elif convert == 2:
    num = int(input("Enter a number:"))
    print(format(num, "o"))

elif convert == 3:
    num = int(input("Enter a number:"))
    print(format(num, "x"))
else:
    print("“Invalid input. Please try again.”")



