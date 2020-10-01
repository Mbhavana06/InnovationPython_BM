# 1. Question 1:

try:
    eval('a=0')

except SyntaxError as e:
    print(e)

# Question 2:
from sys import argv

file_name = argv[1]

while True:
    try:
        with open(file_name, 'r') as file:
            File_content = file.read()
            print(File_content)
            break
    except:
        print("File name is wrong!")
        Re_try = input("Try again?")
        if Re_try == "Yes":
            file_name = input("Enter the file name again:")
        elif Re_try == "No":
            break

# Question 3:

class Error(Exception):
    """Base class for our custom exceptions"""
    pass

class ValueTooLargeError(Error):
    """Exception when Value is too large"""
    pass

class ValueTooSmallError(Error):
    """Exception when Value is too small"""
    pass

def enterNumber(n):
    while True:
        try:
            n = str(input("Enter your number: "))
            if (len(n) > 4):
                raise ValueTooLargeError
            if (len(n) < 4):
                raise ValueTooSmallError
            break
        except ValueTooLargeError:
            print("This value is too large")
            print()
        except ValueTooSmallError:
            print("This value is too small")
            print()
    print("Congrats! You entered a perfect 4 digit code")

enterNumber(0)

# Question 4:
Pass=input("Enter Password")
Counter=0

while True:
    try:
        Retype_Pass = input("Re-enter Password")
        if Pass==Retype_Pass:
            print("Login Successful")
            break
        else:
            raise Exception
    except:
        if Counter<3:
            Counter+=1
        else:
            print("Try again later.")
            break
# Question 5: Complete!


# Question 6:

with open('doc1','r') as text_file:
    for i in text_file:
        i=i.split()
        for e in i:
            if len(e)%2==0:
                print(e)

